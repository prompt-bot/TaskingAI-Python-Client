# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

import pprint
import re  # noqa: F401

import six

class FunctionCreateRequest(object):
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
    swagger_types = {
        'name': 'object',
        'description': 'object',
        'parameters': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, description=None, parameters=None):  # noqa: E501
        """FunctionCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._parameters = None
        self.discriminator = None
        self.name = name
        self.description = description
        self.parameters = parameters

    @property
    def name(self):
        """Gets the name of this FunctionCreateRequest.  # noqa: E501

        A meaningful function name, consists of letters, digits and underscore \"_\" and its first character cannot be a digit.  # noqa: E501

        :return: The name of this FunctionCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FunctionCreateRequest.

        A meaningful function name, consists of letters, digits and underscore \"_\" and its first character cannot be a digit.  # noqa: E501

        :param name: The name of this FunctionCreateRequest.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this FunctionCreateRequest.  # noqa: E501

        The function description.  # noqa: E501

        :return: The description of this FunctionCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FunctionCreateRequest.

        The function description.  # noqa: E501

        :param description: The description of this FunctionCreateRequest.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def parameters(self):
        """Gets the parameters of this FunctionCreateRequest.  # noqa: E501

        The action parameter schema.  # noqa: E501

        :return: The parameters of this FunctionCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this FunctionCreateRequest.

        The action parameter schema.  # noqa: E501

        :param parameters: The parameters of this FunctionCreateRequest.  # noqa: E501
        :type: object
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FunctionCreateRequest, dict):
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
        if not isinstance(other, FunctionCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
