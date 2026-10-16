$savedIoEncoding = $env:PYTHONIOENCODING
try {
    $env:PYTHONIOENCODING = 'utf-8'
    $encodingReport = python -c "import sys; print(sys.stdout.encoding)"
    $encodingReport
} finally {
    if ($null -eq $savedIoEncoding) {
        Remove-Item Env:PYTHONIOENCODING -ErrorAction SilentlyContinue
    } else {
        $env:PYTHONIOENCODING = $savedIoEncoding
    }
}
