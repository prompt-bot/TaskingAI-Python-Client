# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

import pprint
import re  # noqa: F401

import six


class RecordUpdateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"type": "object", "content": "object", "text_splitter": "object", "metadata": "object"}

    attribute_map = {"type": "type", "content": "content", "text_splitter": "text_splitter", "metadata": "metadata"}

    def __init__(self, type=None, content=None, text_splitter=None, metadata=None):  # noqa: E501
        """RecordUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._content = None
        self._text_splitter = None
        self._metadata = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if content is not None:
            self.content = content
        if text_splitter is not None:
            self.text_splitter = text_splitter
        if metadata is not None:
            self.metadata = metadata

    @property
    def type(self):
        """Gets the type of this RecordCreateRequest.  # noqa: E501

        The record type.

        :return: The type of this RecordCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecordCreateRequest.

        The record type.

        :param type: The type of this RecordCreateRequest.  # noqa: E501
        :type: object
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def content(self):
        """Gets the content of this RecordCreateRequest.  # noqa: E501

        The record content.

        :return: The content of this RecordCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this RecordCreateRequest.

        The record content.

        :param content: The content of this RecordCreateRequest.  # noqa: E501
        :type: object
        """

        self._content = content

    @property
    def text_splitter(self):
        """Gets the text_splitter of this RecordCreateRequest.  # noqa: E501

        The text splitter to split records into chunks.

        :return: The text_splitter of this RecordCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._text_splitter

    @text_splitter.setter
    def text_splitter(self, text_splitter):
        """Sets the text_splitter of this RecordCreateRequest.

        The text splitter to split records into chunks.

        :param text_splitter: The text_splitter of this RecordCreateRequest.  # noqa: E501
        :type: object
        """

        self._text_splitter = text_splitter

    @property
    def metadata(self):
        """Gets the metadata of this RecordUpdateRequest.  # noqa: E501


        :return: The metadata of this RecordUpdateRequest.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RecordUpdateRequest.


        :param metadata: The metadata of this RecordUpdateRequest.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(RecordUpdateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecordUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
