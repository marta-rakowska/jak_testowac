import config_reader

configuration = config_reader.load()

print(configuration)
print(configuration[0].strip('\n'))
print(configuration[1].strip('\n'))