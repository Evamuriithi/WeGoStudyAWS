import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods

class WegostudyAppPostiveTestCases(unittest.TestCase):

    @staticmethod
    def test_main_wegostudy():
        methods.setUp()
        methods.log_in()
        methods.create_new_student()
        # methods.create_new_application()
        # methods.view_details()
        # methods.view_application_list()
        methods.sort_by_dropdown_menu()
        methods.commissions()
        methods.filter_by_study_area()
        methods.filter_by_city()
        methods.filter_by_program()
        methods.add_my_favorite()
        methods.connect_to_wegostudy()
        methods.visit_college_website()
        methods.tuition()
        methods.apply_now()
        methods.study_area_prog_lev()
        methods.log_out()
        methods.tearDown()
