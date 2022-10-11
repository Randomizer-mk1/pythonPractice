
"""list of benefits

    Returns:
        string: meh
    """


# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code use"]



    """_summary_

    Returns:
        _type_: _description_
    """
# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % (benefit)
   
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
   

name_the_benefits_of_functions()
