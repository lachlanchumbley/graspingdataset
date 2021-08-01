

class gripperController:
    def __init__(self):
        pass

    def close_gripper(self):
        pass

    def open_gripper(self):
        pass

    def get_gripper_width(self):
        pass
        
    def retract_gripper(self, grasp):
        #use grasp orientation to retract using moveit function
        pass

    def rotate_gripper(self):
        pass

    def object_in_gripper_check(self):
        # attempt to close gripper and check using get_gripper_width() if the gripper fully closes
        # return Bool
        return grasp_successful

