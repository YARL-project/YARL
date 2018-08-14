# Copyright 2018 The RLgraph authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
from rlgraph.agents import DQNAgent, ApexAgent
from rlgraph.environments import OpenAIGymEnv
from rlgraph.tests.test_util import config_from_path


class TestAllCompile(unittest.TestCase):
    """
    Tests if all agents compile correctly on relevant configurations.
    """
    def test_dqn_compilation(self):
        """
        Creates a DQNAgent and runs it via a Runner on an openAI Pong Env.
        """
        env = OpenAIGymEnv("Pong-v0", frameskip=4, max_num_noops=30, random_start=True, episodic_life=True)
        agent_config = config_from_path("configs/dqn_agent_for_pong.json")
        agent = DQNAgent.from_spec(
            # Uses 2015 DQN parameters as closely as possible.
            agent_config,
            state_space=env.state_space,
            # Try with "reduced" action space (actually only 3 actions, up, down, no-op)
            action_space=env.action_space
        )

    def test_apex_compilation(self):
        """
        Tests agent compilation without Ray to ease debugging on Windows.
        """
        agent_config = config_from_path("configs/ray_apex_for_pong.json")
        agent_config["execution_spec"].pop("ray_spec")
        environment = OpenAIGymEnv("Pong-v0", frameskip=4)

        agent = ApexAgent.from_spec(
            agent_config, state_space=environment.state_space, action_space=environment.action_space
        )
        print('Compiled apex agent')


