

vehicle_inventory={}

class Automobile:
    def __init__(self,ID, make,model,color,year,mileage):
        self.ID = ID #user created integer used to organize and recall the correct vehicle information
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage= mileage
        vehicle_inventory[ID]={'Make':make,'Model':model,'Color':color,'Year':year,'Mileage':mileage}

    def add_vehicle(ID):    
        make=input('Make:').upper() #all uppercase to create consistency in dictionary and lists
        model=input('Model:').upper() #all uppercase to create consistency in dictionary and lists
        color=input('Color:').upper() #all uppercase to create consistency in dictionary and lists
        try:
            year=int(input('Year:')) #uses integers to avoid input errors
        except ValueError:
            year=int(input('Please input valid year:'))
        try:
            mileage=int(input('Mileage:')) #uses integers to avoid input errors
        except ValueError:
            mileage=int(input('Please input valid integer:'))
        
        ID=Automobile(ID,make,model,color,year,mileage) #creates dictionary entry
            
    def update_vehicle(ID):
        try:
            if ID in vehicle_inventory:
                print('\n')
                print('Inventory Update Menu')
                print('Update Vehicle ID %d\n' %ID)
                print(' 1. Make\n',
                      '2. Model\n',
                      '3. Color\n',
                      '4. Year\n',
                      '5. Mileage\n',
                      '6. Update all attributes\n',
                      '7. Choose new Inventory ID to update\n'
                      ' 0. Return to Vehicle Inventory Menu\n')

                selection=input('Select option:')

                if selection=='1':
                    make=input('Enter New Make:').upper()
                    vehicle_inventory[ID]['Make']=make
                    print('Make for %d UPDATED to %s.' %(ID,make))
                    Automobile.update_vehicle(ID)

                elif selection=='2':
                    model=input('Enter New Model:').upper()
                    vehicle_inventory[ID]['Model']=model
                    print('Model for %d UPDATED to %s.' %(ID,model))
                    Automobile.update_vehicle(ID)                   

                elif selection=='3':
                    color=input('Enter New Color:').upper()
                    vehicle_inventory[ID]['Color']=color
                    print('Color for %d UPDATED to %s.' %(ID,color))
                    Automobile.update_vehicle(ID)
                    
                elif selection=='4':
                    try:
                        year=int(input('Enter New Year:'))
                    except ValueError:
                        year=int(input('Please input valid year:'))
                    vehicle_inventory[ID]['Year']=year
                    print('Year for %d UPDATED to %d.' %(ID,year))
                    Automobile.update_vehicle(ID)

                elif selection=='5':
                    try:
                        mileage=int(input('Enter New Mileage:'))
                    except:
                        mileage=int(input('Please input valid integer:'))
                    vehicle_inventory[ID]['Mileage']=mileage
                    print('Mileage for %d UPDATED to %d.' %I(ID,mileage))
                    Automobile.update_vehicle(ID)

                elif selection=='6':
                    Automobile.add_vehicle(ID)
                    print('Vehicle %d UPDATED.' %ID)
                    Automobile.update_vehicle(ID)

                elif selection=='7':
                    try:
                        ID=int(input('Enter Inventory ID number:'))
                        Automobile.update_vehicle(ID)
                    except ValueError:
                        print('Invalid Inventory ID number.\n')
                        ID=int(input('Enter Inventory ID number or 0 to quit:'))
                        if ID!=0 and ID in vehicle_inventory:
                            Automobile.update_vehicle(ID)
                            main_menu()
                        else:
                            main_menu()               
                    if ID not in vehicle_inventory:
                        print('ID %d does not exist\n' %ID)
                        ID=int(input('Enter Inventory ID number or 0 to quit:'))
                        if ID in vehicle_inventory:
                            Automobile.update_vehicle(ID)
                            main_menu()
                        else:
                            main_menu()            
                    else:
                        Automobile.update_vehicle(ID)
                        main_menu()
        
                elif selection=='0':
                    main_menu()
                    
                else:
                    print('Invalid selection. Select New Option:')
                    Automobile.update_vehicle(ID)
                    
        except:
            print('Invalid Inventory ID number\n')
            Automobile.update_vehicle(ID)

 
    def remove_vehicle():
        try:
            ID=int(input('Enter Inventory ID number to remove:'))
            del vehicle_inventory[ID]
            print('Vehicle %d removed from inventory.' %ID)
            main_menu()
            
        except KeyError:
            print('Invalid Inventory ID number.\n')
            ID=int(input('Enter Inventory ID number to remove or 0 to quit:'))
            if ID!=0 and ID in vehicle_inventory:
                del vehicle_inventory[ID]
                print('Vehicle %d removed from inventory.' %ID)
                main_menu()
            else:
                main_menu()
           
def get_attribute(val):
    result={}    
    for key, subdict in vehicle_inventory.items():
            while val in subdict.values():
                result[key]=vehicle_inventory[key]
                break
            
    if len(result)==0:
        print('No Vehicles Found.')
    for k, v in result.items():
        print(k, ':', v)
                   
def vehicle_search():
    print('\n')
    print('Vehicle Inventory Search')
    print('Search by:')
    print(' 1. Make\n',
          '2. Model\n',
          '3. Color\n',
          '4. Year\n',
          '5. Inventory ID\n',
          '0. Return to Vehicle Inventory Menu\n')
    selection=input('Select Option:')

    if selection=='1':
            val=input('Make:').upper()
            get_attribute(val)
            vehicle_search()

    elif selection=='2':
            val=input('Enter Model:').upper()
            get_attribute(val)
            vehicle_search()         
            
    elif selection=='3':
            val=input('Enter Color:').upper()
            get_attribute(val)
            vehicle_search()         

    elif selection=='4':
        try:
            val=int(input('Enter Year:'))
            get_attribute(val)
            vehicle_search()
        except ValueError:
            year=int(input('Please input valid year:'))
            get_attribute(val)
            vehicle_search()

    elif selection=='5':
        try:
            ID=int(input('Enter Inventory ID number:'))
            print(vehicle_inventory[ID],'\n')
            vehicle_search()
        except KeyError:
            print('Inventory ID not on file.\n')
            ID=int(input('Enter Inventory ID number or 0 to quit:'))
            if ID!=0:
                print(vehicle_inventory[ID],'\n')
                vehicle_search()
            else:
                main_menu()
    elif selection=='0':
        main_menu()
        
    else:
        print('Invalid selection. Select New Option:')
        vehicle_search()

def main_menu():
    print('\n')
    print('Vehicle Inventory Control\n')
    print(' 1. Add a new vehicle\n',
          '2. Remove a vehicle\n',
          '3. Update a vehicle\n',
          '4. Vehicle Inventory Search\n',
          '5. View full inventory\n',
          '6. Export full inventory to file\n',
          '0. Exit\n')
    
    selection=input('Select option:')

    if selection=='1':
        try:
            ID=int(input('Enter Inventory ID number:'))
        except ValueError:
            print('Invalid Inventory ID number.\n')
            ID=int(input('Enter Inventory ID number or 0 to quit:'))
            if ID!=0:
                Automobile.add_vehicle(ID)
                print('Vehicle %d added to inventory.' %ID)
                main_menu()
            else:
                main_menu()               
        if ID in vehicle_inventory:
            print('Inventory ID already exists.\n')
            ID=int(input('Enter Inventory ID number or 0 to quit:'))
            if ID!=0 and ID not in vehicle_inventory:
                Automobile.add_vehicle(ID)
                print('Vehicle %d added to inventory.' %ID)
                main_menu()
            else:
                main_menu()            
        else:
            Automobile.add_vehicle(ID)
            print('Vehicle %d added to inventory.' %ID)
            main_menu()

    elif selection=='2':
        Automobile.remove_vehicle()
        
    elif selection=='3':
        try:
            ID=int(input('Enter Inventory ID number:'))
        except ValueError:
            print('Invalid Inventory ID number.\n')
            ID=int(input('Enter Inventory ID number or 0 to quit:'))
            if ID!=0 and ID in vehicle_inventory:
                Automobile.update_vehicle(ID)
                main_menu()
            else:
                main_menu()               
        if ID not in vehicle_inventory:
            print('ID %d does not exist.\n' %ID)
            ID=int(input('Enter Inventory ID number or 0 to quit:'))
            if ID!=0 and ID in vehicle_inventory:
                Automobile.update_vehicle(ID)
                main_menu()
            else:
                main_menu()            
        else:
            Automobile.update_vehicle(ID)
            main_menu()
                          
    elif selection=='4':    
        vehicle_search()

    elif selection=='5':
        print('\n')
        print('Total Vehicles in Inventory:',len(vehicle_inventory),'\n')
        for k, v in sorted(vehicle_inventory.items()):
            print(k, ':', v)
        main_menu()
        
    elif selection=='6': 
        with open('vehicle_inventory.txt','w') as file:
            file.write("Vehicle Inventory \n")
            for k in sorted (vehicle_inventory.keys()):
                file.write("'%s':'%s', \n" % (k, vehicle_inventory[k]))
        print('Vehicle Inventory exported to text file.')
        main_menu()
                       
    elif selection=='0':
        print('Goodbye!')
        exit()
    else:
        print('Invalid selection. Select New Option:')
        main_menu()


          
main_menu()

