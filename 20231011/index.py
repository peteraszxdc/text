
import datasource

def main():
    names=datasource.cityNames()
    city=datasource.info(name='連江縣莒光鄉')
    print(names)
    print(city)
if __name__=="__main__":
    main()
