class user_profile:
    users=[]
    def __init__(self,user_id:int,user_name:str,phno:str,email_id:str,password:str):
        self.user_id=user_id
        self.user_name=user_name
        self.phno=phno 
        self.email_id=email_id 
        self.password=password

class movies_profile:
    movies=[]
    def __init__(self,movie_id:int,movie_name:str,time:str,rating:float):
        self.movie_id=movie_id 
        self.movie_name=movie_name 
        self.time=time 
        self.rating=rating 

class movie_functinality(movies_profile):
    def display_info(self):
        for movie in self.movies:
            print(movie.movie_id,'\t',movie.movie_name,'\t',movie.time,'\t',movie.rating)

    def select_movie(self):
        select_movie_name=int(input('Enter your prefer movie : '))
        for i in self.movies:
            if i.movie_id==select_movie_name:
                return i.movie_name

class theater_profile:
    theaters=[]
    def __init__(self,theater_id:int,theater_name:str,location:str,ratings:float,movies:list,show_time):
        self.theater_id=theater_id 
        self.theater_name=theater_name 
        self.location=location 
        self.ratings=ratings 
        self.movies=movies
        self.show_time=show_time 

class theater_functinality(theater_profile):
    def display(self,selected_movie_name):
        for theater in self.theaters:
            for j in theater.movies:
                if j==selected_movie_name:
                    print(theater.theater_id,'\t',theater.theater_name,'\t',theater.location,'\t',theater.ratings)
    
    def selct_theater(self):
        select_theater=int(input('Select your prefer theater id : '))
        for theater in self.theaters:
            if theater.theater_id==select_theater:
                return theater.theater_name 
            
    def display_timings(self,selcted_theater_name):
        for i in self.theaters:
            if i.theater_name==selcted_theater_name:
                [print(key,value) for key,value in i.show_time.items()] 
        return [theater.show_time for theater in self.theaters if theater.theater_name==selcted_theater_name]

    def select_movie_time(self,selcted_theater_name):
        show_tie=self.display_timings(selcted_theater_name)
        selcte_movie_time=int(input('Enter your prefer timing : '))
        if selcte_movie_time>0 and selcte_movie_time<=4 :
            return show_tie[0][selcte_movie_time] 
        
class seat_data:
    seats_data=[]
    def __init__(self,theater_name,show_timeing):
        self.theater_name=theater_name 
        self.show_timing=show_timeing 
        self.seats=[['A1','A2','A3','A4'],['A5','A6','A7','A8'],['A9','A10','A11','A12'],['A13','A14','A15','A16']]


class seat_func:
    def display_seat(self,selcted_theater_name,select_movie_timing):
        re=[i.seats for i in seat_data.seats_data if i.theater_name==selcted_theater_name and i.show_timing==select_movie_timing]
        if re==[]:
            new_seats=seat_data(selcted_theater_name,select_movie_timing)
            seat_data.seats_data.append(new_seats) 
            self.display_seat(selcted_theater_name,select_movie_timing) 
        else:
            for seat_deatils in seat_data.seats_data:
                if seat_deatils.theater_name == selcted_theater_name and seat_deatils.show_timing == select_movie_timing:
                    for rows in seat_deatils.seats:
                        print(*rows)

    def select_theater_seat(self,selcted_theater_name,select_movie_timing):
        self.display_seat(selcted_theater_name,select_movie_timing) 
        [print(i.seats) for i in seat_data.seats_data if i.theater_name==selcted_theater_name and i.show_timing==select_movie_timing]
        re_seat=[i.seats for i in seat_data.seats_data if i.theater_name==selcted_theater_name and i.show_timing==select_movie_timing]
        requested_seats = input("\nEnter the seats as space separated to select:(Ex. A1 A2 A3)\n").upper().split(' ')
        selected_seats=[]
        for rows in re_seat[0]:
            for seat in rows:
                if seat in requested_seats:
                    selected_seats.append(seat)
        
        if len(selected_seats) == len(requested_seats):
            for rows in re_seat[0]:
                for i in range(len(rows)):
                    if rows[i] in selected_seats:
                        rows[i] = '0 '
            return selected_seats

class loginside:
    def validate_login(self,email,password=None):
        re_mail_id=[user.email_id for user in user_profile.users if user.email_id==email]
        if re_mail_id==[] and password==None:
            return True 
        else:
            check_password=[user.password for user in user_profile.users if user.password==password] 
            if re_mail_id and check_password:
                return True 
            
    def signup(self):
        self.user_id=(user_profile.users[-1].user_id)+1
        self.name=input('Enter your name : \t')
        self.check_phno()
        self.email_id=input('Enter your email id : \t').lower()
        self.password=input('Enter your valid password : \t')
        self.check()

    def check(self): 
        p=input('Retype your password : \t')
        if p==self.password:
            if self.validate_login(self.email_id):
                new_user=user_profile(self.user_id,self.name,self.phno,self.email_id,self.password)
                user_profile.users.append(new_user)
        else:
            print('Sorry! Retype your password\t')
            self.check()

    def check_phno(self):
        self.phno=int(input('Enter your phno : \t'))
        if len(str(self.phno))==10:
            return self.phno
        else:
            print('Sorry! your phno size is ',len(str(self.phno)))
            print('Retype your valid phno')
            self.check_phno()

    def login(self):
        email_id=input('Enter your email_id : \t').lower()
        password=input('Enter your password : ')
        if self.validate_login(email_id,password):
            return email_id

class theater_selction(loginside,movie_functinality,theater_functinality,seat_func):
    def __init__(self):
        self.mail_id=None
        self.stay_in=True
    def signup_or_login(self):
        self.p=int(input('1:Signup/2:Login : \t'))
        if self.p==1:
            self.mail_id=self.signup()
            if not self.mail_id:
                print('Already exists')
                self.stay_in=False
        else:
            self.mail_id=self.login()
            if not self.mail_id:
                print('Invalid email id and password')
                self.stay_in=False  
                
    def run(self):
        while self.stay_in:
            print('************************************\n')
            print("Menu:")
            print("1. Book Movie")
            print("2. Display Booking history")
            print("3. Delete Booking history")
            print("4. Logout")
            choice=int(input('Enter your choice : \t'))
            if choice==1:
                self.book_movie()
            elif choice==4:
                print('Logout successfully!')
                self.stay_in=False
    def book_movie(self):
        self.display_info()
        selct_movie_name=self.select_movie()
        if not selct_movie_name:
            print('Invalid movie id')
            return
        print('************************poo',selct_movie_name)
        self.display(selct_movie_name) 
        selcted_theater_name=self.selct_theater()
        if not selcted_theater_name:
            print('Invalid theater')
            self.display(selct_movie_name) 
        select_movie_timing=self.select_movie_time(selcted_theater_name)
        if not select_movie_timing:
            print('Invalid timing')
            return
        
        select_seat=self.select_theater_seat(selcted_theater_name,select_movie_timing)
        if not select_seat:
            print('Invalid seat')
            return 
        
        


if __name__=='__main__':
    user1=user_profile(1,'Priya','8072649175','priya*2003@gmail.com','Priya*2003')
    user2=user_profile(2,'Banu','9067254836','banu*2002@gmail.com','Banu89')
    user3=user_profile(4,'Nivi','9023787789','nivi*990@gmail.com','Nivi78')
    user_profile.users.append(user1)
    user_profile.users.append(user2)
    user_profile.users.append(user3)

    movie1=movies_profile(1,'Joe','2hr 30 mins',4.3)
    movie2=movies_profile(2,'Leo','2hr 45 mins',3.9)
    movie3=movies_profile(3,'Ayothi','2hr 10 mins',4.6)
    movies_profile.movies.append(movie1)
    movies_profile.movies.append(movie2)
    movies_profile.movies.append(movie3)

    theater1=theater_profile(1,'Srivalli','Perungullathur',4.3,['Joe','Leo','Ayothi'],{1:'7:30 AM',2:'10:30 AM',3:'1:30 PM',4:'4:00 PM'})
    theater2=theater_profile(2,'Parvathi','Perungudi',4,['Joe','Leo'],{1:'7:30 AM',2:'10:30 AM',3:'1:30 PM',4:'4:00 PM'})
    theater3=theater_profile(3,'Muthu','Vandalur',3.9,['Joe','Ayothi'],{1:'7:30 AM',2:'10:30 AM',3:'1:30 PM',4:'4:00 PM'})
    theater_profile.theaters.append(theater1)
    theater_profile.theaters.append(theater2)
    theater_profile.theaters.append(theater3)

    theater=theater_selction()
    theater.signup_or_login()
    theater.run()

