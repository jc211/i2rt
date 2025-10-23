import enum
from abc import abstractmethod
from typing import Any, Dict, Protocol, Union, runtime_checkable

import numpy as np


@enum.unique
class RobotType(enum.Enum):
    ARM = "arm"
    MOBILE_BASE = "mobile_base"


@runtime_checkable
class Robot(Protocol):
    """A generic Robot protocol."""

    @abstractmethod
    def num_dofs(self) -> int:
        """Get the number of controllable degrees of freedom of the robot.

        Returns:
            int: The number of controllable degrees of freedom of the robot.
        """
        raise NotImplementedError

    def get_joint_pos(self) -> np.ndarray:
        """Get the current joint positions of the robot in radians.

        Returns:
            np.ndarray: The current joint positions of the robot in radians.
        """
        pass

    def get_joint_state(self) -> Dict[str, np.ndarray]:
        """Get the current joint positions and velocities of the robot in radians.

        Returns:
            Dict[str, np.ndarray]: A dictionary containing the current joint positions and velocities of the robot in radians.
        """
        pass

    def command_joint_pos(self, joint_pos: np.ndarray) -> None:
        """Command the leader robot to a given state.

        Args:
            joint_pos (np.ndarray): The state to command the leader robot to.
        """
        pass

    def command_target_vel(self, joint_vel: np.ndarray) -> None:
        """Command the leader robot to a given state.

        Args:
            joint_vel (np.ndarray): The state to command the leader robot to.
        """
        pass

    def command_joint_state(self, joint_state: Dict[str, np.ndarray]) -> None:
        """Command the leader robot to a given state.

        Args:
            joint_state (Dict[str, np.ndarray]): The state to command the leader robot to.
        """
        pass

    @abstractmethod
    def get_observations(self) -> Dict[str, np.ndarray]:
        """Get the current observations of the robot.

        This is to extract all the information that is available from the robot,
        such as joint positions, joint velocities, etc. This may also include
        information from additional sensors, such as cameras, force sensors, etc.

        Returns:
            Dict[str, np.ndarray]: A dictionary of observations.
        """
        raise NotImplementedError


    def get_robot_info(self) -> Dict[str, Any]:
        """Get the robot information, such as kp, kd, joint limits, gripper limits, etc."""
        return {}

    def get_robot_type(self) -> RobotType:
        """Get the robot type."""
        return RobotType.ARM
