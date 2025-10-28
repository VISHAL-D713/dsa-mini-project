class MovieTicketSystem:
    def __init__(self):
        # Hashmap for booking history (user_id -> list of bookings)
        self.booking_history = {}
        
        # Queue for waiting list (using list as a simple queue)
        self.waiting_list = []
        
        # Stack for cancellation history (using list as a stack)
        self.cancellation_stack = []
        
        # Available seats for each show
        self.available_seats = {
            "show1": 50,
            "show2": 50,
            "show3": 50
        }
        
        # Ticket price
        self.ticket_price = 10
    
    def book_ticket(self, user_id, show_id, num_tickets):
        """Book tickets for a user"""
        print(f"\n--- Booking tickets for user {user_id} ---")
        
        # Check if seats are available
        if self.available_seats[show_id] >= num_tickets:
            # Reduce available seats
            self.available_seats[show_id] -= num_tickets
            
            # Create booking record
            booking = {
                "show_id": show_id,
                "num_tickets": num_tickets,
                "total_cost": num_tickets * self.ticket_price
            }
            
            # Add to booking history
            if user_id not in self.booking_history:
                self.booking_history[user_id] = []
            self.booking_history[user_id].append(booking)
            
            print(f"Successfully booked {num_tickets} tickets for {show_id}!")
            print(f"Total cost: ${booking['total_cost']}")
            print(f"Remaining seats for {show_id}: {self.available_seats[show_id]}")
            
        else:
            # Add to waiting list (queue)
            waiting_request = {
                "user_id": user_id,
                "show_id": show_id,
                "num_tickets": num_tickets
            }
            self.waiting_list.append(waiting_request)
            print(f"Sorry, not enough seats available. Added to waiting list.")
            print(f"Your position in waiting list: {len(self.waiting_list)}")
    
    def cancel_ticket(self, user_id, show_id, num_tickets):
        """Cancel tickets for a user"""
        print(f"\n--- Cancelling tickets for user {user_id} ---")
        
        # Check if user has bookings
        if user_id not in self.booking_history:
            print("No bookings found for this user.")
            return
        
        # Find and remove the booking
        for booking in self.booking_history[user_id]:
            if booking["show_id"] == show_id and booking["num_tickets"] >= num_tickets:
                # Update booking
                booking["num_tickets"] -= num_tickets
                
                # Add to cancellation stack
                cancellation_record = {
                    "user_id": user_id,
                    "show_id": show_id,
                    "num_tickets": num_tickets,
                    "refund_amount": num_tickets * self.ticket_price
                }
                self.cancellation_stack.append(cancellation_record)
                
                # Increase available seats
                self.available_seats[show_id] += num_tickets
                
                print(f"Successfully cancelled {num_tickets} tickets for {show_id}!")
                print(f"Refund amount: ${cancellation_record['refund_amount']}")
                
                # Check waiting list (process queue)
                self._process_waiting_list(show_id)
                return
        
        print("No matching booking found to cancel.")
    
    def _process_waiting_list(self, show_id):
        """Process waiting list when seats become available"""
        if not self.waiting_list:
            return
        
        # Process from front of queue (FIFO)
        temp_waiting_list = []
        
        for request in self.waiting_list:
            if request["show_id"] == show_id and self.available_seats[show_id] >= request["num_tickets"]:
                # Book tickets for waiting list user
                self.available_seats[show_id] -= request["num_tickets"]
                
                # Add to booking history
                if request["user_id"] not in self.booking_history:
                    self.booking_history[request["user_id"]] = []
                
                booking = {
                    "show_id": show_id,
                    "num_tickets": request["num_tickets"],
                    "total_cost": request["num_tickets"] * self.ticket_price
                }
                self.booking_history[request["user_id"]].append(booking)
                
                print(f"Automatically booked {request['num_tickets']} tickets for user {request['user_id']} from waiting list!")
            else:
                # Keep in waiting list
                temp_waiting_list.append(request)
        
        self.waiting_list = temp_waiting_list
    
    def show_booking_history(self, user_id):
        """Show booking history for a user"""
        print(f"\n--- Booking History for user {user_id} ---")
        
        if user_id not in self.booking_history or not self.booking_history[user_id]:
            print("No booking history found.")
            return
        
        for i, booking in enumerate(self.booking_history[user_id], 1):
            print(f"{i}. Show: {booking['show_id']}, Tickets: {booking['num_tickets']}, Cost: ${booking['total_cost']}")
    
    def show_cancellation_history(self):
        """Show recent cancellations (from stack)"""
        print(f"\n--- Recent Cancellations (Last 5) ---")
        
        if not self.cancellation_stack:
            print("No cancellation history.")
            return
        
        # Show last 5 cancellations (LIFO)
        recent_cancellations = self.cancellation_stack[-5:] if len(self.cancellation_stack) > 5 else self.cancellation_stack
        
        for i, cancellation in enumerate(reversed(recent_cancellations), 1):
            print(f"{i}. User: {cancellation['user_id']}, Show: {cancellation['show_id']}, "
                  f"Tickets: {cancellation['num_tickets']}, Refund: ${cancellation['refund_amount']}")
    
    def show_waiting_list(self):
        """Show current waiting list"""
        print(f"\n--- Current Waiting List ---")
        
        if not self.waiting_list:
            print("Waiting list is empty.")
            return
        
        for i, request in enumerate(self.waiting_list, 1):
            print(f"{i}. User: {request['user_id']}, Show: {request['show_id']}, Tickets: {request['num_tickets']}")
    
    def show_available_seats(self):
        """Show available seats for all shows"""
        print(f"\n--- Available Seats ---")
        for show_id, seats in self.available_seats.items():
            print(f"{show_id}: {seats} seats available")

# Demo function to test the system
def demo_system():
    system = MovieTicketSystem()
    
    print("=== MOVIE TICKET MANAGEMENT SYSTEM ===")
    
    # Show initial available seats
    system.show_available_seats()
    
    # Book some tickets
    system.book_ticket("user1", "show1", 3)
    system.book_ticket("user2", "show1", 5)
    system.book_ticket("user3", "show2", 2)
    
    # Try to book when not enough seats
    system.book_ticket("user4", "show1", 50)  # This should go to waiting list
    
    # Show booking history
    system.show_booking_history("user1")
    system.show_booking_history("user2")
    
    # Show waiting list
    system.show_waiting_list()
    
    # Cancel some tickets
    system.cancel_ticket("user1", "show1", 2)
    
    # Show cancellation history
    system.show_cancellation_history()
    
    # Show updated available seats
    system.show_available_seats()
    
    
    system.show_waiting_list()


if __name__ == "__main__":
    demo_system()