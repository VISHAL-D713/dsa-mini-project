🎬 Movie Ticket Management System
A Python-based movie ticket booking system that demonstrates practical implementation of fundamental data structures for efficient ticket management.

🚀 Live Demo
Experience the system live: Movie Ticket Booking App

📚 Data Structures Implementation
HashMap → Booking History
Purpose: Fast user booking lookup

Implementation: Python dictionary storing user_id → list_of_bookings

Usage: Instant access to user's complete booking history

Queue → Waiting List
Purpose: Fair first-come-first-served system

Implementation: List-based FIFO queue

Usage: Manages overflow when shows are fully booked

Stack → Cancellation History
Purpose: Track recent cancellations

Implementation: List-based LIFO stack

Usage: Maintains cancellation records for auditing

🎯 Key Features
✅ Book tickets with automatic seat allocation

✅ Cancel tickets with instant refund processing

✅ Waiting list management for sold-out shows

✅ Complete booking history per user

✅ Real-time seat availability tracking

✅ Automatic waiting list processing on cancellations

💻 Technology Stack
Language: Python 3.x

Data Structures: HashMap, Queue, Stack

Concepts: OOP, Exception Handling, Modular Design

🏫 College Project Relevance
This project perfectly demonstrates:

Real-world application of data structures

Object-Oriented Programming principles

System design thinking

Problem-solving with appropriate data structures

📋 Sample Usage
python
# Initialize system
system = MovieTicketSystem()

# Book tickets
system.book_ticket("student123", "show1", 2)

# Cancel tickets
system.cancel_ticket("student123", "show1", 1)

# View history
system.show_booking_history("student123")
🎓 Learning Outcomes
After studying this project, you'll understand:

When to use HashMap vs Queue vs Stack

How data structures solve real problems

System design considerations

Code organization best practices
