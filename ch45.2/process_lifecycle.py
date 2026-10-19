# process_lifecycle.py
import multiprocessing

def result_child(sender, value, fail):
    try:
        if fail:
            raise ValueError("child rejected value")
        sender.send(("ok", value * value))
    finally:
        sender.close()

def waiting_child(sender, stop):
    try:
        sender.send("ready")
        stop.wait()
    finally:
        try:
            sender.send("cleaned")
        finally:
            sender.close()

def receive_reply(receiver):
    if not receiver.poll(5):
        raise TimeoutError("child reply did not become ready")
    try:
        return receiver.recv(), False
    except EOFError:
        return None, True

def close_owned_child(process, receiver, sender, stop=None):
    forced = False
    try:
        if stop is not None:
            stop.set()
        if process.pid is not None:
            process.join(timeout=5)
            if process.is_alive():
                forced = True
                process.terminate()  # exceptional last resort, not cooperative stop
                process.join(timeout=5)
            if process.is_alive():
                raise RuntimeError("child could not be stopped")
        process.close()
        process_closed = False
        try:
            process.is_alive()
        except ValueError:
            process_closed = True
    finally:
        receiver.close()
        sender.close()
    if forced:
        raise TimeoutError("child required forced termination")
    return {
        "receiver_closed": receiver.closed,
        "sender_closed": sender.closed,
        "process_closed": process_closed,
        "forced_termination": forced,
    }

def observe_result(value, *, fail=False):
    context = multiprocessing.get_context("spawn")
    receiver, sender = context.Pipe(duplex=False)
    process = context.Process(
        target=result_child, args=(sender, value, fail), name="result-child"
    )
    try:
        process.start()
        sender.close()  # parent no longer owns a live sending endpoint
        message, eof = receive_reply(receiver)
        joined = process.join(timeout=5)
        if process.is_alive():
            raise TimeoutError("child did not finish after its reply")
        report = {
            "message": message, "eof": eof, "join_return": joined,
            "alive": process.is_alive(), "exitcode": process.exitcode,
            "pid": process.pid,
        }
    finally:
        resources = close_owned_child(process, receiver, sender)
    report.update(resources)
    return report

def observe_stop():
    context = multiprocessing.get_context("spawn")
    receiver, sender = context.Pipe(duplex=False)
    stop = context.Event()
    process = context.Process(
        target=waiting_child, args=(sender, stop), name="waiting-child"
    )
    try:
        process.start()
        sender.close()
        ready, eof = receive_reply(receiver)
        assert ready == "ready" and not eof
        short_join = process.join(timeout=0)
        alive_after_short_join = process.is_alive()
        exitcode_after_short_join = process.exitcode
        assert alive_after_short_join and exitcode_after_short_join is None
        stop.set()
        cleaned, eof = receive_reply(receiver)
        assert cleaned == "cleaned" and not eof
        completed_join = process.join(timeout=5)
        if process.is_alive():
            raise TimeoutError("child ignored cooperative stop")
        report = {
            "ready": ready, "cleaned": cleaned,
            "short_join_return": short_join,
            "alive_after_short_join": alive_after_short_join,
            "exitcode_after_short_join": exitcode_after_short_join,
            "completed_join_return": completed_join,
            "alive": process.is_alive(), "exitcode": process.exitcode,
            "pid": process.pid,
        }
    finally:
        resources = close_owned_child(process, receiver, sender, stop)
    report.update(resources)
    return report

def main():
    success = observe_result(3)
    failure = observe_result(3, fail=True)
    stopped = observe_stop()
    print("success:", success["message"], "exit:", success["exitcode"])
    print("failure EOF:", failure["eof"], "exit:", failure["exitcode"])
    print("short join:", stopped["short_join_return"], "alive:", stopped["alive_after_short_join"])
    print("completed join:", stopped["completed_join_return"], "cleanup:", stopped["cleaned"])
    print("cooperative stop exit:", stopped["exitcode"])
    reports = (success, failure, stopped)
    print("all resources closed:", all(
        item["receiver_closed"] and item["sender_closed"] and item["process_closed"]
        for item in reports
    ))

if __name__ == "__main__":
    main()
