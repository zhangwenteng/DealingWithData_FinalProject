"""Generated client library for bigquery version v2."""

from googlecloudapis.apitools.base.py import base_api
from googlecloudapis.bigquery.v2 import bigquery_v2_messages as messages


class BigqueryV2(base_api.BaseApiClient):
  """Generated client library for service bigquery version v2."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'bigquery'
  _SCOPES = [u'https://www.googleapis.com/auth/bigquery', u'https://www.googleapis.com/auth/bigquery.insertdata', u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/devstorage.full_control', u'https://www.googleapis.com/auth/devstorage.read_only', u'https://www.googleapis.com/auth/devstorage.read_write']
  _VERSION = u'v2'
  _CLIENT_ID = ''
  _CLIENT_SECRET = ''
  _USER_AGENT = ''
  _CLIENT_CLASS_NAME = u'BigqueryV2'
  _URL_VERSION = u'v2'

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new bigquery handle."""
    url = url or u'https://www.googleapis.com/bigquery/v2/'
    super(BigqueryV2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.datasets = self.DatasetsService(self)
    self.jobs = self.JobsService(self)
    self.projects = self.ProjectsService(self)
    self.tabledata = self.TabledataService(self)
    self.tables = self.TablesService(self)

  class DatasetsService(base_api.BaseApiService):
    """Service class for the datasets resource."""

    _NAME = u'datasets'

    def __init__(self, client):
      super(BigqueryV2.DatasetsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'bigquery.datasets.delete',
              ordered_params=[u'projectId', u'datasetId'],
              path_params=[u'datasetId', u'projectId'],
              query_params=[u'deleteContents'],
              relative_path=u'projects/{projectId}/datasets/{datasetId}',
              request_field='',
              request_type_name=u'BigqueryDatasetsDeleteRequest',
              response_type_name=u'BigqueryDatasetsDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.datasets.get',
              ordered_params=[u'projectId', u'datasetId'],
              path_params=[u'datasetId', u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}',
              request_field='',
              request_type_name=u'BigqueryDatasetsGetRequest',
              response_type_name=u'Dataset',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigquery.datasets.insert',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets',
              request_field=u'dataset',
              request_type_name=u'BigqueryDatasetsInsertRequest',
              response_type_name=u'Dataset',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.datasets.list',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[u'all', u'maxResults', u'pageToken'],
              relative_path=u'projects/{projectId}/datasets',
              request_field='',
              request_type_name=u'BigqueryDatasetsListRequest',
              response_type_name=u'DatasetList',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'bigquery.datasets.patch',
              ordered_params=[u'projectId', u'datasetId'],
              path_params=[u'datasetId', u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}',
              request_field=u'dataset',
              request_type_name=u'BigqueryDatasetsPatchRequest',
              response_type_name=u'Dataset',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'bigquery.datasets.update',
              ordered_params=[u'projectId', u'datasetId'],
              path_params=[u'datasetId', u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}',
              request_field=u'dataset',
              request_type_name=u'BigqueryDatasetsUpdateRequest',
              response_type_name=u'Dataset',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes the dataset specified by the datasetId value. Before you can delete a dataset, you must delete all its tables, either manually or by specifying deleteContents. Immediately after deletion, you can create another dataset with the same name.

      Args:
        request: (BigqueryDatasetsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BigqueryDatasetsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns the dataset specified by datasetID.

      Args:
        request: (BigqueryDatasetsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dataset) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a new empty dataset.

      Args:
        request: (BigqueryDatasetsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dataset) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists all the datasets in the specified project to which the caller has read access; however, a project owner can list (but not necessarily get) all datasets in his project.

      Args:
        request: (BigqueryDatasetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DatasetList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. This method supports patch semantics.

      Args:
        request: (BigqueryDatasetsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dataset) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource.

      Args:
        request: (BigqueryDatasetsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Dataset) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class JobsService(base_api.BaseApiService):
    """Service class for the jobs resource."""

    _NAME = u'jobs'

    def __init__(self, client):
      super(BigqueryV2.JobsService, self).__init__(client)
      self._method_configs = {
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.jobs.get',
              ordered_params=[u'projectId', u'jobId'],
              path_params=[u'jobId', u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/jobs/{jobId}',
              request_field='',
              request_type_name=u'BigqueryJobsGetRequest',
              response_type_name=u'Job',
              supports_download=False,
          ),
          'GetQueryResults': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.jobs.getQueryResults',
              ordered_params=[u'projectId', u'jobId'],
              path_params=[u'jobId', u'projectId'],
              query_params=[u'maxResults', u'pageToken', u'startIndex', u'timeoutMs'],
              relative_path=u'projects/{projectId}/queries/{jobId}',
              request_field='',
              request_type_name=u'BigqueryJobsGetQueryResultsRequest',
              response_type_name=u'GetQueryResultsResponse',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigquery.jobs.insert',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/jobs',
              request_field=u'job',
              request_type_name=u'BigqueryJobsInsertRequest',
              response_type_name=u'Job',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.jobs.list',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[u'allUsers', u'maxResults', u'pageToken', u'projection', u'stateFilter'],
              relative_path=u'projects/{projectId}/jobs',
              request_field='',
              request_type_name=u'BigqueryJobsListRequest',
              response_type_name=u'JobList',
              supports_download=False,
          ),
          'Query': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigquery.jobs.query',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/queries',
              request_field=u'queryRequest',
              request_type_name=u'BigqueryJobsQueryRequest',
              response_type_name=u'QueryResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          'Insert': base_api.ApiUploadInfo(
              accept=['*/*'],
              max_size=None,
              resumable_multipart=True,
              resumable_path=u'/resumable/upload/bigquery/v2/projects/{projectId}/jobs',
              simple_multipart=True,
              simple_path=u'/upload/bigquery/v2/projects/{projectId}/jobs',
          ),
          }

    def Get(self, request, global_params=None):
      """Retrieves the specified job by ID.

      Args:
        request: (BigqueryJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def GetQueryResults(self, request, global_params=None):
      """Retrieves the results of a query job.

      Args:
        request: (BigqueryJobsGetQueryResultsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetQueryResultsResponse) The response message.
      """
      config = self.GetMethodConfig('GetQueryResults')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None, upload=None):
      """Starts a new asynchronous job.

      Args:
        request: (BigqueryJobsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        upload: (Upload, default: None) If present, upload
            this stream with the request.
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Insert')
      upload_config = self.GetUploadConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params,
          upload=upload, upload_config=upload_config)

    def List(self, request, global_params=None):
      """Lists all the Jobs in the specified project that were started by the user. The job list returns in reverse chronological order of when the jobs were created, starting with the most recent job created.

      Args:
        request: (BigqueryJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (JobList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Query(self, request, global_params=None):
      """Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout.

      Args:
        request: (BigqueryJobsQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (QueryResponse) The response message.
      """
      config = self.GetMethodConfig('Query')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(BigqueryV2.ProjectsService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.projects.list',
              ordered_params=[],
              path_params=[],
              query_params=[u'maxResults', u'pageToken'],
              relative_path=u'projects',
              request_field='',
              request_type_name=u'BigqueryProjectsListRequest',
              response_type_name=u'ProjectList',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists the projects to which you have at least read access.

      Args:
        request: (BigqueryProjectsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProjectList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class TabledataService(base_api.BaseApiService):
    """Service class for the tabledata resource."""

    _NAME = u'tabledata'

    def __init__(self, client):
      super(BigqueryV2.TabledataService, self).__init__(client)
      self._method_configs = {
          'InsertAll': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigquery.tabledata.insertAll',
              ordered_params=[u'projectId', u'datasetId', u'tableId'],
              path_params=[u'datasetId', u'projectId', u'tableId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll',
              request_field=u'tableDataInsertAllRequest',
              request_type_name=u'BigqueryTabledataInsertAllRequest',
              response_type_name=u'TableDataInsertAllResponse',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.tabledata.list',
              ordered_params=[u'projectId', u'datasetId', u'tableId'],
              path_params=[u'datasetId', u'projectId', u'tableId'],
              query_params=[u'maxResults', u'pageToken', u'startIndex'],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data',
              request_field='',
              request_type_name=u'BigqueryTabledataListRequest',
              response_type_name=u'TableDataList',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def InsertAll(self, request, global_params=None):
      """Streams data into BigQuery one record at a time without needing to run a load job.

      Args:
        request: (BigqueryTabledataInsertAllRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TableDataInsertAllResponse) The response message.
      """
      config = self.GetMethodConfig('InsertAll')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves table data from a specified set of rows.

      Args:
        request: (BigqueryTabledataListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TableDataList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class TablesService(base_api.BaseApiService):
    """Service class for the tables resource."""

    _NAME = u'tables'

    def __init__(self, client):
      super(BigqueryV2.TablesService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'bigquery.tables.delete',
              ordered_params=[u'projectId', u'datasetId', u'tableId'],
              path_params=[u'datasetId', u'projectId', u'tableId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
              request_field='',
              request_type_name=u'BigqueryTablesDeleteRequest',
              response_type_name=u'BigqueryTablesDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.tables.get',
              ordered_params=[u'projectId', u'datasetId', u'tableId'],
              path_params=[u'datasetId', u'projectId', u'tableId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
              request_field='',
              request_type_name=u'BigqueryTablesGetRequest',
              response_type_name=u'Table',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigquery.tables.insert',
              ordered_params=[u'projectId', u'datasetId'],
              path_params=[u'datasetId', u'projectId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables',
              request_field=u'table',
              request_type_name=u'BigqueryTablesInsertRequest',
              response_type_name=u'Table',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigquery.tables.list',
              ordered_params=[u'projectId', u'datasetId'],
              path_params=[u'datasetId', u'projectId'],
              query_params=[u'maxResults', u'pageToken'],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables',
              request_field='',
              request_type_name=u'BigqueryTablesListRequest',
              response_type_name=u'TableList',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'bigquery.tables.patch',
              ordered_params=[u'projectId', u'datasetId', u'tableId'],
              path_params=[u'datasetId', u'projectId', u'tableId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
              request_field=u'table',
              request_type_name=u'BigqueryTablesPatchRequest',
              response_type_name=u'Table',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'bigquery.tables.update',
              ordered_params=[u'projectId', u'datasetId', u'tableId'],
              path_params=[u'datasetId', u'projectId', u'tableId'],
              query_params=[],
              relative_path=u'projects/{projectId}/datasets/{datasetId}/tables/{tableId}',
              request_field=u'table',
              request_type_name=u'BigqueryTablesUpdateRequest',
              response_type_name=u'Table',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted.

      Args:
        request: (BigqueryTablesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BigqueryTablesDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table.

      Args:
        request: (BigqueryTablesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Table) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a new, empty table in the dataset.

      Args:
        request: (BigqueryTablesInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Table) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists all tables in the specified dataset.

      Args:
        request: (BigqueryTablesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TableList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics.

      Args:
        request: (BigqueryTablesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Table) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource.

      Args:
        request: (BigqueryTablesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Table) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)
