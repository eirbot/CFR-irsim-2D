import irsim

def main():

    env = irsim.make('robot_world.yaml') # initialize the environment with the configuration file

    for i in range(300): # run the simulation for 300 steps

        env.step()  # update the environment
        env.render() # render the environment

        if env.done(): 
            break # check if the simulation is done

    env.end() # close the environment


if __name__ == "__main__":
    main()
