import ex1


if __name__ == "__main__":
    base_hcreature = ex1.HealingCreatureFactory().create_base()
    evo_hcreature = ex1.HealingCreatureFactory().create_evolved()
    base_tcreature = ex1.TransformCreatureFactory().create_base()
    evo_tcreature = ex1.TransformCreatureFactory().create_evolved()
    print(f"""Testing creature with healing capability
  base
{base_hcreature.describe()}
{base_hcreature.attack()}
{base_hcreature.heal()}
  evolved
{evo_hcreature.describe()}
{evo_hcreature.attack()}
{evo_hcreature.heal()}

Testing creature with transform ability
  base
{base_tcreature.describe()}
{base_tcreature.attack()}
{base_tcreature.transform()}
{base_tcreature.attack()}
{base_tcreature.revert()}
  evolved
{evo_tcreature.describe()}
{evo_tcreature.attack()}
{evo_tcreature.transform()}
{evo_tcreature.attack()}
{evo_tcreature.revert()}
""")
