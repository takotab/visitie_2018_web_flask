from visitatie.make_indeling import make_indeling


def test_make_indeling():
    list_of_users = {'1'  : {"constraint": ['2', '1']},
                     '2'  : {"constraint": ['3', '2', '1']},
                     '3'  : {"constraint": ['1', '2']},
                     '11' : {"constraint": ['12']},
                     '12' : {"constraint": ['13']},
                     '13' : {"constraint": ['11', '3', '4']},
                     '111': {"constraint": ['121', '3', '2', '1']},
                     '121': {"constraint": ['131', ]},
                     '131': {"constraint": ['111', '3', '2', '1']},
                     }
    list_of_users['1']['constraint'].append('3')
    indeling, output_str = make_indeling(list_of_users)
    assert type(output_str) == str
