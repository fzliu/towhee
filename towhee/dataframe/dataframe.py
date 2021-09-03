# Copyright 2021 Zilliz. All rights reserved.
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


from towhee.dataframe._iterator import ScalarIterator
from towhee.dataframe._iterator import GroupIterator
from towhee.dataframe._iterator import BatchIterator
from towhee.dataframe._iterator import RepeatIterator


class DataFrame:
    """A dataframe is a collection of immutable, potentially heterogeneous blogs of
    data.
    """

    def __init__(self, name: str, data: list[tuple[Variable]] = None):
        """DataFrame constructor.

        Args:
            name:
                Name of the dataframe; `DataFrame` names should be the same as its
                representation.
            data:
                A list of data tuples - in all instances, the number of elements per
                tuple should be identical throughout the entire lifetime of the
                `Dataframe`. These tuples can be interpreted as being direct outputs
                into downstream operators.
        """
        self._iter = ScalarIterator(df)
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

    def __getitem__(self, val):
        return data[val]

    def __delete__(self, val):
        del data[val]

    def append(self, item: tuple[Variable]):
        data.append(item)

    def iter_scalar(self):
        #TODO(fzliu): register iterator
        return iter(ScalarIterator(self._df))

    def iter_group_by(self, func: function):
        return iter(GroupIterator(self._df, func))

    def iter_batch(self, size: int):
        return iter(BatchIterator(self._df, size))

    def iter_repeat(self, n: int):
        return iter(RepeatIterator(self._df, n))
