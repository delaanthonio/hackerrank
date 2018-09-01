#!/usr/bin/env python3

from typing import List

MIN_LEN = 1


def prefixes(row: str) -> List[int]:
    new_row = [-1]
    for i, x in enumerate(row):
        if x == '.':
            new_row.append(new_row[i] + 1)
        else:
            new_row.append(-1)
    return tuple(new_row[1:])


def kmarsh(marsh: List[str]) -> int:
    prfx_rows = [prefixes(row) for row in marsh]
    prfx_cols = [prefixes(col) for col in zip(*marsh)]
    prfx_cols = [col for col in zip(*prfx_cols)]
    max_area = 0
    for bt in range(MIN_LEN, len(marsh)):
        for rt in range(MIN_LEN, len(marsh[0])):
            ptl_h = prfx_cols[bt][rt]
            ptl_w = prfx_rows[bt][rt]
            ptl_area = 2 * (ptl_h + ptl_w)
            if ptl_h < MIN_LEN or ptl_w < MIN_LEN or ptl_area < max_area:
                continue
            for lf in range(rt - ptl_w, rt):
                if prfx_cols[bt][lf] < MIN_LEN:
                    continue
                w = rt - lf
                for tp in range(bt - ptl_h, bt):
                    if prfx_rows[tp][rt] < MIN_LEN:
                        continue
                    h = bt - tp
                    if prfx_rows[tp][rt] >= w and prfx_cols[bt][lf] >= h:
                        area = 2 * (h + w)
                        if area > max_area:
                            max_area = area
                        break
    return max_area


def main():
    m, n = [int(x) for x in input().strip().split()]
    marsh = [input().strip() for _ in range(m)]
    area = kmarsh(marsh)
    if not area:
        print("impossible")
    else:
        print(area)


if __name__ == '__main__':
    main()
