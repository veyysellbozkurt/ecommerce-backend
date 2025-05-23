# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command group for Artifact Registry packages."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.UniverseCompatible
class Packages(base.Group):
  """Manage Artifact Registry packages.

  ## EXAMPLES
  To list all packages in the current project and `artifacts/repository` and
  `artifacts/location` properties are set,
  run:

      $ {command} list

  To list packages under repository my-repo in the current project and location,
  run:

      $ {command} list --repository=my-repo

  To delete package `my-pkg` under repository my-repo in the current project and
  location, run:

      $ {command} delete my-pkg --repository=my-repo
  """

  category = base.CI_CD_CATEGORY
