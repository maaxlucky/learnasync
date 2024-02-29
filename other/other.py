print('This will always be run')

def main():
    print(f'First Module Name: {__name__}')

if __name__ == '__main__':
    main()
    print(f'Run directly')
else:
    print(f'Run From Import')

# print("Always executed")

# if __name__ == "__main__":
    # print("Executed when invoked directly")
# else:
    # print("Executed when imported")



