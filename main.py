if __name__ == "__main__":
  # Python Delete File

  import os

  try:
    os.remove("readme.txt")
  except FileNotFoundError as error:
    print(error)
