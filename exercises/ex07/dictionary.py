"""Dictionary for EX07."""

__author__ = "730602160"


def invert(reg_dict: dict[str, str]) -> dict[str, str]:
    """Switches X and Y."""
    inv_dict: dict[str, str] = {}
    for element in reg_dict:
        if reg_dict[element] in inv_dict:
            raise KeyError("Equal Values Detected.")
        else:
            inv_dict[reg_dict[element]] = element
    return inv_dict


def favorite_color(color: dict[str, str]) -> str:
    """Returns most frequent Y."""
    refer: dict[str, int] = {}
    list_colors: list[str] = []
    for key in color:
        if color[key] not in list_colors:
            refer[color[key]] = 1
            list_colors.append(color[key])
        else:
            refer[color[key]] += 1
    index_max: int = 0
    color_max: str = ""
    for key in refer:
        if refer[key] > index_max:
            index_max = refer[key]
            color_max = key
    return color_max                   


def count(frequency: list[str]) -> dict[str, int]:
    """Returns present values and how many times they appear."""
    subject: dict[str, int] = {}
    for index in frequency:
        if index not in subject:
            subject[index] = 1
        else:
            subject[index] += 1
    return subject            