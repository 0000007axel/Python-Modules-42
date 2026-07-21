import alchemy.grimoire


if __name__ == "__main__":
    thing: str = alchemy.grimoire.light_spell_record('Fantasy',
                                                     'Tea, haha and FiRe')
    print(f"""=== Kaboom 0 ===
Using grimoire module directly
Testing record light spell: {thing}
""")
