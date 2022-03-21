# Method for converting RGB to hexadecimal
def rgb_hex():
  # error message
  invalid_msg = "Invalid value. Please try again"

  # asking user for R value
  red = int(raw_input("Enter R: "))
  if (red < 0 or red > 255):
    print invalid_msg
    return 

  # asking user for G value
  green = int(raw_input("Enter G: "))
  if (green < 0 or green > 255):
    print invalid_msg
    return 

  # asking user for B value
  blue = int(raw_input("Enter B: "))
  if (blue < 0 or blue > 255):
    print invalid_msg
    return 

  # optimization using bitwise operator
  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()

# method for converting Hexadecimal to RGB
def hex_rgb():
  hex_val = raw_input("Enter your hexadecimal value: "
  )
  if (hex_val != 6):
    print "Invalid input. PLease try again."
    return
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2 ** 8
  
  # calculating the red value
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8 

  # calculating the green value
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8

  # calculating the red value
  red = hex_val % two_hex_digits
  hex_val = hex_val >> 8

  print "Red: %s Green: %s Blue: %s" % (red, green, blue)

# Main method 
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if (option == "1"):
      print "RGB to Hex..."
      rgb_hex()
    elif (option == "2"):
      print "Hex to RGB..."
      hex_rgb()
    elif (option == "x" or option == "X"):
      break
    else: 
      print "Error."

convert()


