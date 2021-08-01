# 0.  Initalise an algorithm
# 1.  Position arm to first bin position (centre of clutter / table)
# 2.  Take Point Cloud 
# 3.  Convert/Stitch input point cloud
# 4.  Input point cloud to grasping algorithm (start with agilegrasp2)
# 5.  Recieve output: Grasps and their qualities
# 6.  Randomly (w/ bias) select a grasp quality and select closest grasp quality
# 7.  Move arm to grasp position
# 8.  Close gripper
# 9.  Move back in reverse direction of gripper orientation
# 10. Move upwards
# 11. Move to standard position above new tub and do a rotation
# 12. Check if object is still in gripper (force closure method)
# 13. Move down and drop
# 14. Repeat from step 0 -> until no objects left in tub (grasp detection qualities below certain threshold? or max no. of grasps?)
# 15. Move to next bin
# 16. Repeat Step 14
# 17. Move to centre bin
# 18. Move 15 objects to bin 1 and 15 to bin 2
# 19. Initalise an algorithm
# 20. Repeat from start

import random
from gripperUtils import *
from armUtils import *


class GraspingDataCollection:
    
    def __init__(self):
        
        # this needs to be a ros-service, post processig tuple
        self.armControl = armControl()
        self.gripperControl = gripperController()
        self.algorithms = [('agile_grasp2','SERVICE', self.post_process_agile)]
        self.MAX_ITERATION = 50
        self.OBJECT_CHECK_HEIGHT = 1


    def sample_algorithm(self):
        self.current_alg = random.choice(self.algorithms)   

    def post_process_agile(self, output_format):
        #take weird output format and put it to a standard format
        pass       
    
    def take_point_cloud(self):
        # take point cloud from RGBD camera in ROS point cloud 
        return point_cloud
    
    def stitch_point_clouds(self, point_clouds):
        # stitch together the given set of point clouds into a single point cloud
        return stitched_point_cloud

    def perform_current_algorithm(self, point_cloud, algorithm):
        # algorithm (ros-service, post processing function) as a tuple
        # peform given algorthim on given point cloud and output post-processed grasp 
        return post_processed_grasps

    def select_grasp(self, algorithm_name, post_processed_grasps):
        # generate random value with bias, selected grasp with closest quality value and output grasp
        successfulGrasps, unsuccesfulGrasps = self.count_grasps(algorithm_name)
        return grasp
        
    def count_grasps(self, algorithm_name):
        return success, unsuccesful

    def check_for_objects(current_bin):
        return True
    
    def save_grasp(pointcloud, grasp, isSuccess, isRobust):
        pass
    
    def iterate_through_single_bin(self, current_bin, drop_bin):
        
        self.current_bin = current_bin
        self.drop_bin = self.drop_bin

        success_count = 0
        robust_count = 0
        total_count = 0

        isSuccess = False
        isRobust = False
        
        while self.check_for_objects(self.current_bin) or total_count < self.MAX_ITERATION:
            pc = self.take_point_cloud()
            stiched_pc = self.stitch_point_clouds()
            grasps = self.perform_current_algorithm(stiched_pc, self.current_alg)
            final_grasp = self.select_grasp(self.current_alg[0], grasps)
            self.armControl.perform_grasp(final_grasp)
            self.close_gripper()
            self.retract_gripper()
            self.armControl.move_upwards(self.OBJECT_CHECK_HEIGHT)
            
            total_count += 1
            
            if self.gripperControl.object_in_gripper_check():
                isSuccess = True
                success_count += 1
            
            current_drop_bin = random.choice(drop_bin)

            self.armControl.move_to_check_position(current_drop_bin)
            self.gripperControl.rotate_gripper()

            if self.gripperControl.object_in_gripper_check():
                isRobust = True
                robust_count += 1
            
            self.save_grasp(stiched_pc, final_grasp, isSuccess, isRobust)

            if isRobust:
                self.armControl.drop_object(self.drop)
                
            self.gripperControl.open_gripper()
            
    def main(self):
        bin_pairs = [(0, [2]), (1, [2]), (2, [0,1])]
        while True:
            self.sample_algorithm()
            for current_bin, drop_bin in bin_pairs:
                self.iterate_through_single_bin(current_bin, drop_bin)

            
        