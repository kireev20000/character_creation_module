def we_crash_all(name: str) -> str:
    return 'Привет, ' + name + ', мы всё сломали!'

print(we_crash_all('Наташа'))

def main(duel_res):
    current_rep = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return f'После {len(duel_res)} поединков,' \
           f'' репутация персонажа — {current_rep:.3f} очков.'