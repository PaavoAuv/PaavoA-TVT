def main():
    print("Program starting.")

    try:
        
        r_raw = input("Insert red: ")
        g_raw = input("Insert green: ")
        b_raw = input("Insert blue: ")

       
        r = int(r_raw)
        g = int(g_raw)
        b = int(b_raw)

        
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            raise ValueError("out of range")

        
        hex_value = "#{:02x}{:02x}{:02x}".format(r, g, b)

        
        r_bin = "{:08b}".format(r)
        g_bin = "{:08b}".format(g)
        b_bin = "{:08b}".format(b)

        
        print("RGB Details:")
        print("- Red {}".format(r))
        print("- Green {}".format(g))
        print("- Blue {}".format(b))
        print("- Hex {}".format(hex_value))
        print("- R-byte {}".format(r_bin))
        print("- G-byte {}".format(g_bin))
        print("- B-byte {}".format(b_bin))

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()
