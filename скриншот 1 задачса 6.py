def all_eq(lst):
    ale = max(lst, key=lambda x: len(x))
    poka = len(ale)
    return [item.ljust(poka, '_') for item in lst]
print(all_eq(['мусоровоз', 'фура', 'однофазный_высоковольтный_дискриминант']))