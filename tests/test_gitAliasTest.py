# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import platform
import subprocess
from .utilities.helper import DevopsScenarioTest

class TestGitAliasing(DevopsScenarioTest):
    def test_git_aliases_pr_repo(self):
        self.cmd('az devops configure --use-git-aliases')
        repo_help = subprocess.check_output('git repo -h', shell=platform.system() != "Windows")
        pr_help = subprocess.check_output('git pr -h', shell=platform.system() != "Windows")
