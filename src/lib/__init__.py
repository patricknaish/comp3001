# Initial loader for libraries.  Brings them into the global namespace.

import Course
import Paypal
import University

# Now make the classes available readily
Paypal = Paypal.Paypal
Course = Course.Course
University = University.University
