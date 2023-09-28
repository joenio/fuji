# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model
from fuji_server.models.core_metadata_output import CoreMetadataOutput  # noqa: F401,E501
from fuji_server.models.debug import Debug  # noqa: F401,E501
from fuji_server.models.fair_result_common import FAIRResultCommon  # noqa: F401,E501
from fuji_server.models.fair_result_common_score import FAIRResultCommonScore  # noqa: F401,E501
from fuji_server.models.fair_result_evaluation_criterium import FAIRResultEvaluationCriterium  # noqa: F401,E501


class CoreMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        id: int = None,
        metric_identifier: str = None,
        metric_name: str = None,
        metric_tests: Dict[str, FAIRResultEvaluationCriterium] = None,
        test_status: str = "fail",
        score: FAIRResultCommonScore = None,
        maturity: int = 0,
        output: CoreMetadataOutput = None,
        test_debug: Debug = None,
    ):  # noqa: E501
        """CoreMetadata - a model defined in Swagger

        :param id: The id of this CoreMetadata.  # noqa: E501
        :type id: int
        :param metric_identifier: The metric_identifier of this CoreMetadata.  # noqa: E501
        :type metric_identifier: str
        :param metric_name: The metric_name of this CoreMetadata.  # noqa: E501
        :type metric_name: str
        :param metric_tests: The metric_tests of this CoreMetadata.  # noqa: E501
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        :param test_status: The test_status of this CoreMetadata.  # noqa: E501
        :type test_status: str
        :param score: The score of this CoreMetadata.  # noqa: E501
        :type score: FAIRResultCommonScore
        :param maturity: The maturity of this CoreMetadata.  # noqa: E501
        :type maturity: int
        :param output: The output of this CoreMetadata.  # noqa: E501
        :type output: CoreMetadataOutput
        :param test_debug: The test_debug of this CoreMetadata.  # noqa: E501
        :type test_debug: Debug
        """
        self.swagger_types = {
            "id": int,
            "metric_identifier": str,
            "metric_name": str,
            "metric_tests": Dict[str, FAIRResultEvaluationCriterium],
            "test_status": str,
            "score": FAIRResultCommonScore,
            "maturity": int,
            "output": CoreMetadataOutput,
            "test_debug": Debug,
        }

        self.attribute_map = {
            "id": "id",
            "metric_identifier": "metric_identifier",
            "metric_name": "metric_name",
            "metric_tests": "metric_tests",
            "test_status": "test_status",
            "score": "score",
            "maturity": "maturity",
            "output": "output",
            "test_debug": "test_debug",
        }
        self._id = id
        self._metric_identifier = metric_identifier
        self._metric_name = metric_name
        self._metric_tests = metric_tests
        self._test_status = test_status
        self._score = score
        self._maturity = maturity
        self._output = output
        self._test_debug = test_debug

    @classmethod
    def from_dict(cls, dikt) -> "CoreMetadata":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CoreMetadata of this CoreMetadata.  # noqa: E501
        :rtype: CoreMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this CoreMetadata.


        :return: The id of this CoreMetadata.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this CoreMetadata.


        :param id: The id of this CoreMetadata.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metric_identifier(self) -> str:
        """Gets the metric_identifier of this CoreMetadata.


        :return: The metric_identifier of this CoreMetadata.
        :rtype: str
        """
        return self._metric_identifier

    @metric_identifier.setter
    def metric_identifier(self, metric_identifier: str):
        """Sets the metric_identifier of this CoreMetadata.


        :param metric_identifier: The metric_identifier of this CoreMetadata.
        :type metric_identifier: str
        """
        if metric_identifier is None:
            raise ValueError("Invalid value for `metric_identifier`, must not be `None`")  # noqa: E501

        self._metric_identifier = metric_identifier

    @property
    def metric_name(self) -> str:
        """Gets the metric_name of this CoreMetadata.


        :return: The metric_name of this CoreMetadata.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name: str):
        """Sets the metric_name of this CoreMetadata.


        :param metric_name: The metric_name of this CoreMetadata.
        :type metric_name: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def metric_tests(self) -> Dict[str, FAIRResultEvaluationCriterium]:
        """Gets the metric_tests of this CoreMetadata.


        :return: The metric_tests of this CoreMetadata.
        :rtype: Dict[str, FAIRResultEvaluationCriterium]
        """
        return self._metric_tests

    @metric_tests.setter
    def metric_tests(self, metric_tests: Dict[str, FAIRResultEvaluationCriterium]):
        """Sets the metric_tests of this CoreMetadata.


        :param metric_tests: The metric_tests of this CoreMetadata.
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        """

        self._metric_tests = metric_tests

    @property
    def test_status(self) -> str:
        """Gets the test_status of this CoreMetadata.


        :return: The test_status of this CoreMetadata.
        :rtype: str
        """
        return self._test_status

    @test_status.setter
    def test_status(self, test_status: str):
        """Sets the test_status of this CoreMetadata.


        :param test_status: The test_status of this CoreMetadata.
        :type test_status: str
        """
        allowed_values = ["pass", "fail", "indeterminate"]  # noqa: E501
        if test_status not in allowed_values:
            raise ValueError(
                "Invalid value for `test_status` ({0}), must be one of {1}".format(test_status, allowed_values)
            )

        self._test_status = test_status

    @property
    def score(self) -> FAIRResultCommonScore:
        """Gets the score of this CoreMetadata.


        :return: The score of this CoreMetadata.
        :rtype: FAIRResultCommonScore
        """
        return self._score

    @score.setter
    def score(self, score: FAIRResultCommonScore):
        """Sets the score of this CoreMetadata.


        :param score: The score of this CoreMetadata.
        :type score: FAIRResultCommonScore
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def maturity(self) -> int:
        """Gets the maturity of this CoreMetadata.


        :return: The maturity of this CoreMetadata.
        :rtype: int
        """
        return self._maturity

    @maturity.setter
    def maturity(self, maturity: int):
        """Sets the maturity of this CoreMetadata.


        :param maturity: The maturity of this CoreMetadata.
        :type maturity: int
        """

        self._maturity = maturity

    @property
    def output(self) -> CoreMetadataOutput:
        """Gets the output of this CoreMetadata.


        :return: The output of this CoreMetadata.
        :rtype: CoreMetadataOutput
        """
        return self._output

    @output.setter
    def output(self, output: CoreMetadataOutput):
        """Sets the output of this CoreMetadata.


        :param output: The output of this CoreMetadata.
        :type output: CoreMetadataOutput
        """

        self._output = output

    @property
    def test_debug(self) -> Debug:
        """Gets the test_debug of this CoreMetadata.


        :return: The test_debug of this CoreMetadata.
        :rtype: Debug
        """
        return self._test_debug

    @test_debug.setter
    def test_debug(self, test_debug: Debug):
        """Sets the test_debug of this CoreMetadata.


        :param test_debug: The test_debug of this CoreMetadata.
        :type test_debug: Debug
        """

        self._test_debug = test_debug
