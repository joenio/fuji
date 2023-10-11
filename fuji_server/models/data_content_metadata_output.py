from fuji_server import util
from fuji_server.models.base_model_ import Model
from fuji_server.models.data_content_metadata_output_inner import DataContentMetadataOutputInner  # noqa: F401,E501


class DataContentMetadataOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, object_type: str = None, data_content_descriptor: list[DataContentMetadataOutputInner] = None
    ):  # noqa: E501
        """DataContentMetadataOutput - a model defined in Swagger

        :param object_type: The object_type of this DataContentMetadataOutput.  # noqa: E501
        :type object_type: str
        :param data_content_descriptor: The data_content_descriptor of this DataContentMetadataOutput.  # noqa: E501
        :type data_content_descriptor: List[DataContentMetadataOutputInner]
        """
        self.swagger_types = {"object_type": str, "data_content_descriptor": list[DataContentMetadataOutputInner]}

        self.attribute_map = {"object_type": "object_type", "data_content_descriptor": "data_content_descriptor"}
        self._object_type = object_type
        self._data_content_descriptor = data_content_descriptor

    @classmethod
    def from_dict(cls, dikt) -> "DataContentMetadataOutput":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataContentMetadata_output of this DataContentMetadataOutput.  # noqa: E501
        :rtype: DataContentMetadataOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_type(self) -> str:
        """Gets the object_type of this DataContentMetadataOutput.


        :return: The object_type of this DataContentMetadataOutput.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: str):
        """Sets the object_type of this DataContentMetadataOutput.


        :param object_type: The object_type of this DataContentMetadataOutput.
        :type object_type: str
        """

        self._object_type = object_type

    @property
    def data_content_descriptor(self) -> list[DataContentMetadataOutputInner]:
        """Gets the data_content_descriptor of this DataContentMetadataOutput.


        :return: The data_content_descriptor of this DataContentMetadataOutput.
        :rtype: List[DataContentMetadataOutputInner]
        """
        return self._data_content_descriptor

    @data_content_descriptor.setter
    def data_content_descriptor(self, data_content_descriptor: list[DataContentMetadataOutputInner]):
        """Sets the data_content_descriptor of this DataContentMetadataOutput.


        :param data_content_descriptor: The data_content_descriptor of this DataContentMetadataOutput.
        :type data_content_descriptor: List[DataContentMetadataOutputInner]
        """

        self._data_content_descriptor = data_content_descriptor
