from fuji_server import util
from fuji_server.models.base_model_ import Model


class DataFileFormatOutputInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        file_uri: str = None,
        mime_type: str = None,
        is_preferred_format: bool = False,
        preference_reason: list[str] = None,
        subject_areas: list[str] = None,
    ):  # noqa: E501
        """DataFileFormatOutputInner - a model defined in Swagger

        :param file_uri: The file_uri of this DataFileFormatOutputInner.  # noqa: E501
        :type file_uri: str
        :param mime_type: The mime_type of this DataFileFormatOutputInner.  # noqa: E501
        :type mime_type: str
        :param is_preferred_format: The is_preferred_format of this DataFileFormatOutputInner.  # noqa: E501
        :type is_preferred_format: bool
        :param preference_reason: The preference_reason of this DataFileFormatOutputInner.  # noqa: E501
        :type preference_reason: List[str]
        :param subject_areas: The subject_areas of this DataFileFormatOutputInner.  # noqa: E501
        :type subject_areas: List[str]
        """
        self.swagger_types = {
            "file_uri": str,
            "mime_type": str,
            "is_preferred_format": bool,
            "preference_reason": list[str],
            "subject_areas": list[str],
        }

        self.attribute_map = {
            "file_uri": "file_uri",
            "mime_type": "mime_type",
            "is_preferred_format": "is_preferred_format",
            "preference_reason": "preference_reason",
            "subject_areas": "subject_areas",
        }
        self._file_uri = file_uri
        self._mime_type = mime_type
        self._is_preferred_format = is_preferred_format
        self._preference_reason = preference_reason
        self._subject_areas = subject_areas

    @classmethod
    def from_dict(cls, dikt) -> "DataFileFormatOutputInner":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataFileFormat_output_inner of this DataFileFormatOutputInner.  # noqa: E501
        :rtype: DataFileFormatOutputInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_uri(self) -> str:
        """Gets the file_uri of this DataFileFormatOutputInner.


        :return: The file_uri of this DataFileFormatOutputInner.
        :rtype: str
        """
        return self._file_uri

    @file_uri.setter
    def file_uri(self, file_uri: str):
        """Sets the file_uri of this DataFileFormatOutputInner.


        :param file_uri: The file_uri of this DataFileFormatOutputInner.
        :type file_uri: str
        """

        self._file_uri = file_uri

    @property
    def mime_type(self) -> str:
        """Gets the mime_type of this DataFileFormatOutputInner.


        :return: The mime_type of this DataFileFormatOutputInner.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type: str):
        """Sets the mime_type of this DataFileFormatOutputInner.


        :param mime_type: The mime_type of this DataFileFormatOutputInner.
        :type mime_type: str
        """

        self._mime_type = mime_type

    @property
    def is_preferred_format(self) -> bool:
        """Gets the is_preferred_format of this DataFileFormatOutputInner.


        :return: The is_preferred_format of this DataFileFormatOutputInner.
        :rtype: bool
        """
        return self._is_preferred_format

    @is_preferred_format.setter
    def is_preferred_format(self, is_preferred_format: bool):
        """Sets the is_preferred_format of this DataFileFormatOutputInner.


        :param is_preferred_format: The is_preferred_format of this DataFileFormatOutputInner.
        :type is_preferred_format: bool
        """

        self._is_preferred_format = is_preferred_format

    @property
    def preference_reason(self) -> list[str]:
        """Gets the preference_reason of this DataFileFormatOutputInner.


        :return: The preference_reason of this DataFileFormatOutputInner.
        :rtype: List[str]
        """
        return self._preference_reason

    @preference_reason.setter
    def preference_reason(self, preference_reason: list[str]):
        """Sets the preference_reason of this DataFileFormatOutputInner.


        :param preference_reason: The preference_reason of this DataFileFormatOutputInner.
        :type preference_reason: List[str]
        """

        self._preference_reason = preference_reason

    @property
    def subject_areas(self) -> list[str]:
        """Gets the subject_areas of this DataFileFormatOutputInner.


        :return: The subject_areas of this DataFileFormatOutputInner.
        :rtype: List[str]
        """
        return self._subject_areas

    @subject_areas.setter
    def subject_areas(self, subject_areas: list[str]):
        """Sets the subject_areas of this DataFileFormatOutputInner.


        :param subject_areas: The subject_areas of this DataFileFormatOutputInner.
        :type subject_areas: List[str]
        """

        self._subject_areas = subject_areas
