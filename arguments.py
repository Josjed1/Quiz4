import argparse

def main() -> None: 	
    parser=argparse.ArgumentParser() 
    	
    parser.add_argument(help='Enter a string',dest='string',type=str)         	
    parser.add_argument(help='Enter a integer',dest='number',type=int)   
    parser.add_argument(help='Enter a float',dest='float',type=float)
 
    args = parser.parse_args()  	

    string=args.string
    numbers=args.number  	
    floating=args.float
    

    print("String is: ", string) 	
    print("Integer is:  ",numbers)
    print("Float is: ", floating)

if __name__=='__main__': 	
    main()
