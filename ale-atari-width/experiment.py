#!/usr/bin/python

import sys
import os
import time

def main():

  #PARAMETROS
  
  game = [("Frostbite-v0", "supported_roms/group_1/frostbite.bin")]
  max_sim_steps_per_frame = [25000]
  ratio = [0.25, 0.375, 0.5, 0.625, 0.75]
  
  tiempo = 5
  
  
  #EXPERIMENTACION
  
  for value_game in game:
    for value_max_sim_steps_per_frame in max_sim_steps_per_frame:
        for value_ratio in ratio:
          program = "./ale"
          program += " -display_screen true"
          program += " -discount_factor 0.995"
          program += " -randomize_successor_novelty true"
          program += " -restricted_action_set true"
          program += " -player_agent combination_agent"
          program += " -search_method iw1"
          program += " -max_num_frames 8000"
          program += " -game " + value_game[0]
          program += " -max_sim_steps_per_frame " + str(value_max_sim_steps_per_frame)
          program += " -mode consensus"
          program += " -ratio " + str(value_ratio)
          program += " -images false"
          program += " " + value_game[1]
          
          print "\n===========================================================\n"
          print program            
          print "\n===========================================================\n"
          time.sleep(4) 
          
          os.system(program)

          
            
main()
