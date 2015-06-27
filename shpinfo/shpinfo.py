#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import shapefile

from collections import Counter

field_types = {
    'C': 'Character',
    'N': 'Number',
    'L': 'Long',
    'D': 'Date',
    'M': 'Memo'
}

shape_types = {
    0: 'Null Shape',
    1: 'Point',
    3: 'PolyLine',
    5: 'Polygon',
    8: 'MultiPoint',
    11: 'PointZ',
    13: 'PolyLineZ',
    15: 'PolygonZ',
    18: 'MultiPointZ',
    21: 'PointM',
    23: 'PolyLineM',
    25: 'PolygonM',
    28: 'MultiPointM',
    31: 'MultiPatch'
}


@click.command()
@click.argument('filename')
def main(filename):
    sf = shapefile.Reader(filename)

    print('\nFields\n------\n')
    print('{0:35s}|{1:14s}|{2:>14s}|{3:>14s}'.format('Field Name', 'Field Type', 'Field Length', 'Decimal Length'))
    print('-' * 80)
    for f in sf.fields[1:]:  # omit DeletionFlag
        print('{0:35s}|{1:14s}|{2:14,d}|{3:14d}'.format(f[0], field_types.get(f[1]), f[2], f[3]))

    print('\n\nShapes\n------\n')
    print('{0:35s}|{1:>14s}'.format('Shape Type', 'Count'))
    print('-' * 50)
    shapes = Counter(s.shapeType for s in sf.iterShapes())
    for stype, count in shapes.items():
        print('{0:35s}|{1:14,d}'.format(shape_types.get(stype), count))


if __name__ == '__main__':
    main()
