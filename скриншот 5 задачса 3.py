def count_it(sequence):
    kyky = {int(item): sequence.count(item) for item in sequence}
    puki_puki = sorted(kyky.items(), key=lambda element: element[1])
    return dict(puki_puki[-3:])
print(count_it('5555555552525'))
