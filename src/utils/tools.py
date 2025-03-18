import emoji
import re

def remove_emojis(inputString: str) -> str:
    """Remove emojis from string

    Args:
        inputString (str): Phrase with emojis to remove

    Returns:
        str: String without emojis. Return origin string if it not contain any emoji.
    """
    listCaracteres = [char for char in inputString if not emoji.is_emoji(char)]
    return "".join(listCaracteres)


def remove_punctuation(inputString: str) -> str:
    """Removes non-alphabetic characters, preserving Portuguese-specific characters (accents, ç, etc.).

    Args:
        inputString (str): Phrase with punctuation to remove

    Returns:
        str: String without punctuation. Return origin string if it not contain any punctuation.
    """
    return re.sub(r'[^a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕ ]', '', inputString)


def remove_special_chars(inputString: str) -> str:
    """Removes escape characters such as tabs, newlines, carriage returns, form feeds, and vertical tabs from the input string. 

    Args:
        input_string (str): Phrase with special charecteres to remove

    Returns:
        str: String without special charecteres. Return origin string if it not contain any special charecteres.
    """
    return re.sub(r'[\t\n\r\f\v]', ' ', inputString)


def remove_space_unecessary(inputString: str) -> str:
    """Removes unnecessary spaces from a string

    Args:
        input_string (str): Phrase with space unecessary to remove.

    Returns:
        str: String without space unecessary.
    """
    # Remove leading and trailing spaces
    input_string = inputString.strip()

    # Replace multiple spaces with a single space
    input_string = re.sub(r'\s+', ' ', input_string)

    # Optionally, remove spaces before punctuation
    input_string = re.sub(r'\s([?.!,:;])', r'\1', input_string)

    return input_string