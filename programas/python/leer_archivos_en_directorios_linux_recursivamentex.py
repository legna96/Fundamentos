import os

def main():
  comando = '''cd /kaizen_dev/MICONTA/ && find . -type f -exec stat -c "%n,%s,%w" {} \; > data.txt'''
  os.system(comando)

if __name__ == "__main__":
    main()
