
import datasource

def main():
    cities=datasource.cities_info()
    for city in cities:
        print(cities)
if __name__=="__main__":
    main()
