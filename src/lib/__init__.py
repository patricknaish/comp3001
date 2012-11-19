"""
Root of the libraries behind the web UI for the book trader system.

All classes that are the same name as their modules are brought into the global
namespace
"""
import lib.Course
import lib.Paypal
import lib.University

# Now make the classes available readily
PAYPAL = lib.Paypal.Paypal
COURSE = lib.Course.Course
UNIVERSITY = lib.University.University
