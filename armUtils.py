
class armControl:

    def __init__(self):
        pass

    def perform_grasp(self, grasp):
        # input position and orientation into MoveIt, call function
        pass

    def move_upwards(self, object_check_height):
        # move gripper upwards to desired height
        pass

    def move_to_check_position(self, current_bin):
        # move gripper to check position over current bin
        pass

    def move_to_bin_position(self, current_bin):
        # take current bin number and position gripper above the centre of the bin
        pass

    def drop_object(self, destination_bin):
        # lower it a certain amount, call open_gripper
        pass

