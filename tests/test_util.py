import pytest

from ipwb import util


@pytest.mark.parametrize('expected,input', [
    ('', ''),
    ('foo', 'foo'),
    ('18', '18'),
    ('201l', '201l'),
    ('2018010100000O', '2018010100000O'),
    ('20181', '20181'),
    ('20180001000000', '201800'),
    ('20180132000000', '20180132'),
    ('20180102260000', '2018010226'),
    ('20181301000000', '20181301000000'),
    ('20180932000000', '20180932000000'),
    ('20180230000000', '20180230000000'),
    ('20181126134257.123', '20181126134257.123'),
    ('20180101000000', '2018'),
    ('20181101000000', '201811'),
    ('20181126000000', '20181126'),
    ('20181126130000', '2018112613'),
    ('20181126134200', '201811261342'),
    ('20181126134257', '20181126134257'),
])
def test_pad_digits14(expected, input):
    assert expected == util.pad_digits14(input)


@pytest.mark.parametrize('input', [
    '',
    'foo',
    '18',
    '201l',
    '2018010100000O',
    '20181',
    '201800',
    '20180132',
    '2018010226',
    '20181301000000',
    '20180932000000',
    '20180230000000',
    '20180102263127',
    '20181126134257.123',
])
def test_pad_digits14_inalid(input):
    with pytest.raises(ValueError):
        util.pad_digits14(input, validate=True)
