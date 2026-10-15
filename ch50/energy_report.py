# energy_report.py
from io import StringIO
from math import isfinite
import pandas as pd


FIXTURE = '''batch_id,station,epoch_seconds,cycles,kwh_per_cycle,adjustment_kwh,recovered_kwh
B1,North,0,2,4,1,2
B2,North,3600,3,4,0,0
B3,North,7200,2,6,2,2
B4,South,10800,4,2,0,1
B5,North,14400,,4,0,1
B6,,18000,3,5,0,0
B7,South,21600,1,8,0,2
B8,North,25200,1,4,0,1
'''


def prepare(frame):
    if not frame.index.is_unique or frame['batch_id'].duplicated().any():
        raise ValueError('unique row labels and batch IDs required')
    clean = frame.dropna().copy()
    values = clean['cycles']
    if (not all(isfinite(value) for value in values)
            or values.le(0).any() or values.mod(1).ne(0).any()):
        raise ValueError('known cycle counts must be positive whole numbers')
    converted = values.astype('int64')
    # Both pieces retain the same labels, including gaps left by dropna.
    clean = pd.concat([clean.drop(columns='cycles'), converted], axis=1,
                      join='inner')
    clean['time_utc'] = pd.to_datetime(clean['epoch_seconds'], unit='s',
                                       origin='unix', utc=True)
    clean['gross'] = clean['cycles'] * clean['kwh_per_cycle']
    clean['net'] = (clean['gross'] + clean['adjustment_kwh']
                    - clean['recovered_kwh'])
    if clean['gross'].le(0).any():
        raise ValueError('positive gross energy required for this percentage')
    clean['recovery_percent'] = 100 * clean['recovered_kwh'] / clean['gross']
    return clean


def second_batch(clean, station):
    ordered = clean.loc[clean['station'] == station].sort_values(
        ['net', 'batch_id'], ascending=[False, True])
    if len(ordered) < 2:
        return None
    row = ordered.iloc[1]
    return row['batch_id'], row['time_utc'].isoformat()


def main():
    frame = pd.read_csv(StringIO(FIXTURE))
    original = frame.copy(deep=True)
    complete = frame.dropna()
    print('missing:', {k: int(v) for k, v in frame.isna().sum().items() if v})
    print('cycle dtype:', frame['cycles'].dtype, complete['cycles'].dtype)
    wrong_counts = complete['cycles'].astype('int64').reset_index(drop=True)
    wrong = pd.concat([complete.drop(columns='cycles'), wrong_counts],
                      axis=1, join='inner')
    clean = prepare(frame)
    print('wrong IDs:', wrong['batch_id'].tolist())
    print('kept IDs:', clean['batch_id'].tolist(), 'dtype:', clean['cycles'].dtype)
    print('net energy:', round(float(clean['net'].sum()), 2))
    print('second North batch:', second_batch(clean, 'North'))
    print('rows:', clean.groupby('station').size().to_dict())
    average = clean.groupby('station')['recovery_percent'].mean().round(2)
    totals = clean.groupby('station')[['recovered_kwh', 'gross']].sum()
    weighted = (100 * totals['recovered_kwh'] / totals['gross']).round(2)
    print('mean batch percent:', average.to_dict())
    print('overall percent:', weighted.to_dict())
    print('source unchanged:', frame.equals(original))


if __name__ == '__main__':
    main()
