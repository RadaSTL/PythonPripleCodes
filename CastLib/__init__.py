def intCast(input):
    try:
        int(input)
        return int(input)
    except ValueError:
        print("This is not an integer.")
        return False
    except:
        raise


def stringCast(input):
    try:
        str(input)
        return str(input)
    except ValueError:
        print("This is not a string.")
        return False
    except:
        raise
