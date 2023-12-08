import allure
import pytest

from taskingai.tool import create_function, list_functions, get_function, update_function, delete_function, bulk_create_actions, get_action, update_action, delete_action, run_action, list_actions
from test.common.logger import logger


# @allure.epic("test_sync_tool")
# @allure.feature("test_function")
# @pytest.mark.sync
# class TestFunction:
#
#     function_list = ['object', 'function_id', 'name', 'description', 'parameters', 'created_timestamp']
#     function_keys = set(function_list)
#     function_parameters = ['type', 'properties', 'required']
#     function_parameters_keys = set(function_parameters)
#
#     @pytest.mark.run(order=0)
#     @allure.story("test_create_function")
#     @pytest.mark.parametrize("sync_function_num", (sync_function_num+1 for sync_function_num in range(1, 10)))
#     def test_create_function(self, sync_function_num):
#         # List functions.
#         old_res = list_functions()
#         old_nums = len(old_res)
#         # Create a function.
#         name = f"test{sync_function_num}"
#         description = "test for function"
#         parameters = {
#                             "type": "object",
#                             "properties": {
#                                 "a": {
#                                     "type": "number",
#                                     "description": "First number."
#                                 },
#                                 "b": {
#                                     "type": "number",
#                                     "description": "Second number."
#                                 }
#                             },
#                             "required": ["a", "b"]
#                         }
#
#         res = create_function(name=name, description=description, parameters=parameters)
#         res_dict = res.to_dict()
#         pytest.assume(res_dict.keys() == self.function_keys)
#         pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(res_dict["name"] == name)
#         pytest.assume(res_dict["description"] == description)
#         pytest.assume(res_dict["parameters"] == parameters)
#         # Get a function.
#         get_res = get_function(function_id=res_dict["function_id"])
#         get_res_dict = get_res.to_dict()
#         pytest.assume(get_res_dict.keys() == self.function_keys)
#         pytest.assume(get_res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(get_res_dict["name"] == name)
#         pytest.assume(get_res_dict["description"] == description)
#         pytest.assume(get_res_dict["parameters"] == parameters)
#         # List functions.
#         new_res = list_functions()
#         new_nums = len(new_res)
#         pytest.assume(new_nums == old_nums + 1)
#
#     @pytest.mark.run(order=1)
#     @allure.story("test_list_functions")
#     def test_list_functions(self):
#         # List functions.
#         nums_limit = 4
#         res = list_functions(limit=nums_limit)
#         pytest.assume(len(res) == nums_limit)
#         after_id = res[-1].function_id
#         after_res = list_functions(limit=nums_limit, after=after_id)
#         pytest.assume(len(after_res) == nums_limit)
#         twice_nums_list = list_functions(limit=nums_limit * 2)
#         pytest.assume(len(twice_nums_list) == nums_limit * 2)
#         pytest.assume(after_res[-1] == twice_nums_list[-1])
#         pytest.assume(after_res[0] == twice_nums_list[nums_limit])
#         before_id = after_res[0].function_id
#         before_res = list_functions(limit=nums_limit, before=before_id)
#         pytest.assume(len(before_res) == nums_limit)
#         pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
#         pytest.assume(before_res[0] == twice_nums_list[0])
#
#     @pytest.mark.run(order=2)
#     @allure.story("test_get_function")
#     def test_get_function(self, function_id):
#         # Get a function.
#         res = get_function(function_id=function_id)
#         res_dict = res.to_dict()
#         pytest.assume(res_dict.keys() == self.function_keys)
#         pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
#
#     @pytest.mark.run(order=3)
#     @allure.story("test_update_function")
#     def test_update_function(self, function_id):
#         # Update a function.
#         name = "test"
#         description = "test for function"
#         parameters = {
#             "type": "object",
#             "properties": {
#                 "name": {
#                     "type": "string"
#                 }
#             },
#             "required": ["name"]
#         }
#         res = update_function(function_id=function_id, name=name, description=description, parameters=parameters)
#         res_dict = res.to_dict()
#         pytest.assume(res_dict.keys() == self.function_keys)
#         pytest.assume(res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(res_dict["name"] == name)
#         pytest.assume(res_dict["description"] == description)
#         pytest.assume(res_dict["parameters"] == parameters)
#         # Get a function.
#         get_res = get_function(function_id=function_id)
#         get_res_dict = get_res.to_dict()
#         pytest.assume(get_res_dict.keys() == self.function_keys)
#         pytest.assume(get_res_dict["parameters"].keys() == self.function_parameters_keys)
#         pytest.assume(get_res_dict["name"] == name)
#         pytest.assume(get_res_dict["description"] == description)
#         pytest.assume(get_res_dict["parameters"] == parameters)
#
#     @pytest.mark.run(order=37)
#     @allure.story("test_delete_function")
#     def test_delete_function(self):
#         # List functions.
#         functions = list_functions(limit=100)
#         old_nums = len(functions)
#
#         for index, function in enumerate(functions):
#             function_id = function.function_id
#             # Delete a function.
#             delete_function(function_id=function_id)
#             new_functions = list_functions()
#             function_ids = [function.function_id for function in new_functions]
#             pytest.assume(function_id not in function_ids)
#             new_nums = len(new_functions)
#             pytest.assume(new_nums == old_nums - 1 - index)


@allure.epic("test_sync_tool")
@allure.feature("test_action")
@pytest.mark.sync
class TestAction:

    action_list = ['object', 'action_id', 'name', 'description', 'authentication', 'schema', 'created_timestamp']
    action_keys = set(action_list)
    action_schema = ['openapi', 'info', 'servers', 'paths', 'components', 'security']
    action_schema_keys = set(action_schema)
    schema = {
        "openapi": "3.1.0",
        "info": {
            "title": "Get weather data",
            "description": "Retrieves current weather data for a location.",
            "version": "v1.0.0"
        },
        "servers": [
            {
                "url": "https://weather.example.com"
            }
        ],
        "paths": {
            "/location": {
                "get": {
                    "description": "Get temperature for a specific location",
                    "operationId": "GetCurrentWeather",
                    "parameters": [
                        {
                            "name": "location",
                            "in": "query",
                            "description": "The city and state to retrieve the weather for",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        }
                    ],
                    "deprecated": False
                },
                "post": {
                    "description": "UPDATE temperature for a specific location",
                    "operationId": "UpdateCurrentWeather",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/componeents/schemas/ActionCreateRequest"
                                }
                            }
                        }
                    },
                    "deprecated": False
                }
            }
        },
        "components": {
            "schemas": {}
        },
        "security": []
    }

    @pytest.mark.run(order=4)
    @allure.story("test_bulk_create_actions")
    @pytest.mark.parametrize("sync_action_num", (x+1 for x in range(1, 10)))
    def test_bulk_create_actions(self, sync_action_num):
        # List actions.
        old_res = list_actions(limit=100)
        old_nums = len(old_res)
        # Create an action.
        name = f"GetCurrentWeather{sync_action_num}"
        description = "Get temperature for a specific location"
        res = bulk_create_actions(schema=self.schema)
        for action in res:
            action_dict = action.to_dict()
            logger.info(action_dict)
            pytest.assume(action_dict.keys() == self.action_keys)
            pytest.assume(action_dict["schema"].keys() == self.action_schema_keys)
            # for key, value in self.schema.items():
            for key in action_dict["schema"].keys():
                if key == "paths":
                    if action_dict["schema"][key]["/location"] == "get":
                        pytest.assume(
                            action_dict["schema"][key]["/location"]["get"] == self.schema["paths"]["/location"]["get"])
                    elif action_dict["schema"][key]["/location"] == "post":
                        pytest.assume(
                            action_dict["schema"][key]["/location"]["post"] == self.schema["paths"]["/location"][
                                "post"])
                else:
                    pytest.assume(action_dict["schema"][key] == self.schema[key])
            # Get an action.
            action_id = action_dict["action_id"]
            get_res = get_action(action_id=action_id)
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.action_keys)
            pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)
            # for key, value in self.schema.items():
            for key in action_dict["schema"].keys():
                if key == "paths":
                    if action_dict["schema"][key]["/location"] == "get":
                        pytest.assume(
                            action_dict["schema"][key]["/location"]["get"] == self.schema["paths"]["/location"]["get"])
                    elif action_dict["schema"][key]["/location"] == "post":
                        pytest.assume(
                            action_dict["schema"][key]["/location"]["post"] == self.schema["paths"]["/location"][
                                "post"])
                else:
                    pytest.assume(action_dict["schema"][key] == self.schema[key])
        # List actions.
        new_res = list_actions(limit=100)
        new_nums = len(new_res)
        res_num = len(res)
        pytest.assume(new_nums == old_nums + res_num)

    @pytest.mark.run(order=5)
    @allure.story("test_run_action")
    def test_run_action(self, action_id):
        # Run an action.
        parameters = {
                      "parameters": {"location": "tokyo"}
                     }
        res = run_action(action_id=action_id, parameters=parameters)
        logger.info(f'async run action{res}')
        pytest.assume(res['status'] == 400)
        pytest.assume(res["error"])

    @pytest.mark.run(order=6)
    @allure.story("test_list_actions")
    def test_list_actions(self):
        # List actions.
        nums_limit = 4
        res = list_actions(limit=nums_limit)
        logger.info(res)
        pytest.assume(len(res) == nums_limit)
        after_id = res[-1].action_id
        after_res = list_actions(limit=nums_limit, after=after_id)
        logger.info(after_res)
        pytest.assume(len(after_res) == nums_limit)
        twice_nums_list = list_actions(limit=nums_limit * 2)
        logger.info(twice_nums_list)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])
        before_id = after_res[0].action_id
        before_res = list_actions(limit=nums_limit, before=before_id)
        logger.info(before_res)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=7)
    @allure.story("test_get_action")
    def test_get_action(self, action_id):
        # Get an action.
        res = get_action(action_id=action_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.action_keys)
        logger.info(res_dict["schema"].keys())
        pytest.assume(res_dict["schema"].keys() == self.action_schema_keys)

    @pytest.mark.run(order=39)
    @allure.story("test_update_action")
    def test_update_action(self, action_id):
        # Update an action.
        update_schema = {
            "openapi": "3.1.0",
            "info": {
                "title": "Get weather data",
                "description": "Retrieves current weather data for a location.",
                "version": "v1.0.0"
            },
            "servers": [
                {
                    "url": "https://weather.example.com"
                }
            ],
            "paths": {
                "/location": {
                    "get": {
                        "description": "Get temperature for a specific location by get method",
                        "operationId": "GetCurrentWeather",
                        "parameters": [
                            {
                                "name": "location",
                                "in": "query",
                                "description": "The city and state to retrieve the weather for",
                                "required": True,
                                "schema": {
                                    "type": "string"
                                }
                            }
                        ],
                        "deprecated": False
                    }

                }
            },
            "components": {
                "schemas": {}
            },
            "security": []
        }
        res = update_action(action_id=action_id, schema=update_schema)
        res_dict = res.to_dict()
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.action_keys)
        pytest.assume(res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(res_dict["schema"] == update_schema)
        # for key in res_dict["schema"].keys():
        #     pytest.assume(res_dict["schema"][key] == update_schema[key])
        # Get an action.
        get_res = get_action(action_id=action_id)
        get_res_dict = get_res.to_dict()
        logger.info(get_res_dict)
        pytest.assume(get_res_dict.keys() == self.action_keys)
        # for key in res_dict["schema"].keys():
        #     pytest.assume(res_dict["schema"][key] == update_schema[key])
        pytest.assume(get_res_dict["schema"].keys() == self.action_schema_keys)
        pytest.assume(get_res_dict["schema"] == update_schema)

    @pytest.mark.run(order=40)
    @allure.story("test_delete_action")
    def test_delete_action(self):
        # List actions.
        actions = list_actions(limit=100)
        old_nums = len(actions)

        for index, action in enumerate(actions):
            action_id = action.action_id
            # Delete an action.
            delete_action(action_id=action_id)
            new_actions = list_actions(limit=100)
            action_ids = [action.action_id for action in new_actions]
            pytest.assume(action_id not in action_ids)
            new_nums = len(new_actions)
            pytest.assume(new_nums == old_nums - 1 - index)




