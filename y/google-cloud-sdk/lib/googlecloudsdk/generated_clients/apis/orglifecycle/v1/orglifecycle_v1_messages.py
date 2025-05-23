"""Generated message classes for orglifecycle version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'orglifecycle'


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListManagedOrganizationsResponse(_messages.Message):
  r"""Message for response to listing ManagedOrganizations

  Fields:
    managedOrganizations: The list of ManagedOrganization
    nextPageToken: A token identifying a page of results the server should
      return.
    unreachable: Locations that could not be reached.
  """

  managedOrganizations = _messages.MessageField('ManagedOrganization', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents a Google Cloud location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class ManagedOrganization(_messages.Message):
  r"""This organization managed by GCP resellers.

  Enums:
    StateValueValuesEnum: Output only. The state of the managed organization
      and cloudresourcemanager.googleapis.com/Organization created on behalf
      of the customer.

  Fields:
    admins: Optional. List of organization admins.
    createTime: Output only. The timestamp for the managed organization was
      created.
    deleteTime: Output only. The timestamp that the managed organization was
      soft deleted.
    name: Identifier. The resource name of the managed organization. Format: o
      rganizations/{organization_id}/locations/{location}/managedOrganizations
      /{managed_organization_id}
    organizationDisplayName: Required. Immutable. The display name of the
      cloudresourcemanager.googleapis.com/Organization created on behalf of
      the customer.
    organizationNumber: Output only. System generated ID for the
      cloudresourcemanager.googleapis.com/Organization created on behalf of
      the customer.
    purgeTime: Output only. Time after which the managed organization will be
      permanently purged and cannot be recovered.
    state: Output only. The state of the managed organization and
      cloudresourcemanager.googleapis.com/Organization created on behalf of
      the customer.
    updateTime: Output only. The timestamp for the last update of the managed
      organization.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The state of the managed organization and
    cloudresourcemanager.googleapis.com/Organization created on behalf of the
    customer.

    Values:
      STATE_UNSPECIFIED: State unspecified.
      ACTIVE: The organization of the
        cloudresourcemanager.googleapis.com/Organization created on behalf of
        the customer is soft-deleted.
      DELETED: The organization of the
        cloudresourcemanager.googleapis.com/Organization created on behalf of
        the customer is soft-deleted. Soft-deleted organization are
        permanently deleted after approximately 30 days. You can restore a
        soft-deleted organization using
        [Orglifecycle.UndeleteManagedOrganization]. You cannot reuse the ID of
        a soft-deleted organization until it is permanently deleted.
    """
    STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETED = 2

  admins = _messages.MessageField('OrganizationAdmin', 1, repeated=True)
  createTime = _messages.StringField(2)
  deleteTime = _messages.StringField(3)
  name = _messages.StringField(4)
  organizationDisplayName = _messages.StringField(5)
  organizationNumber = _messages.IntegerField(6)
  purgeTime = _messages.StringField(7)
  state = _messages.EnumField('StateValueValuesEnum', 8)
  updateTime = _messages.StringField(9)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal, successful response of the operation. If the original
    method returns no data on success, such as `Delete`, the response is
    `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: Output only. API version used to start the operation.
    createTime: Output only. The time the operation was created.
    endTime: Output only. The time the operation finished running.
    managedOrganization: Output only. Managed organization information for
      this request
    requestedCancellation: Output only. Identifies whether the user has
      requested cancellation of the operation. Operations that have been
      cancelled successfully have Operation.error value with a
      google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
    statusMessage: Output only. Human-readable status of the operation, if
      any.
    target: Output only. Server-defined resource path for the target of the
      operation.
    verb: Output only. Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  createTime = _messages.StringField(2)
  endTime = _messages.StringField(3)
  managedOrganization = _messages.MessageField('ManagedOrganization', 4)
  requestedCancellation = _messages.BooleanField(5)
  statusMessage = _messages.StringField(6)
  target = _messages.StringField(7)
  verb = _messages.StringField(8)


class OrganizationAdmin(_messages.Message):
  r"""List of admins that will be granted with GCP IAM role:
  roles/resourcemanager.organizationAdmin

  Fields:
    member: Required. Valid IAM principles. See member field under
      https://cloud.google.com/iam/docs/reference/sts/rest/v1/Binding
  """

  member = _messages.StringField(1)


class OrglifecycleOrganizationsLocationsGetRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class OrglifecycleOrganizationsLocationsListRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsListRequest object.

  Fields:
    extraLocationTypes: Optional. A list of extra location types that should
      be used as conditions for controlling the visibility of the locations.
    filter: A filter to narrow down results to a preferred subset. The
      filtering language accepts strings like `"displayName=tokyo"`, and is
      documented in more detail in [AIP-160](https://google.aip.dev/160).
    name: The resource that owns the locations collection, if applicable.
    pageSize: The maximum number of results to return. If not set, the service
      selects a default.
    pageToken: A page token received from the `next_page_token` field in the
      response. Send that page token to receive the subsequent page.
  """

  extraLocationTypes = _messages.StringField(1, repeated=True)
  filter = _messages.StringField(2)
  name = _messages.StringField(3, required=True)
  pageSize = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(5)


class OrglifecycleOrganizationsLocationsManagedOrganizationsCreateRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsManagedOrganizationsCreateRequest
  object.

  Fields:
    managedOrganization: A ManagedOrganization resource to be passed as the
      request body.
    managedOrganizationId: Required. User specified Managed Organization ID.
      This has to be unique under parent:
      organizations/{organization_id}/locations/{location} It must be 6 to 30
      lowercase ASCII letters, digits, or hyphens. It must start with a
      letter.Trailing hyphens are prohibited. Example: tokyo-rain-123
    parent: Required. The parent resource where this ManagedOrganization will
      be created. Must be in the format:
      organizations/{organization_id}/locations/{location}.
  """

  managedOrganization = _messages.MessageField('ManagedOrganization', 1)
  managedOrganizationId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OrglifecycleOrganizationsLocationsManagedOrganizationsDeleteRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsManagedOrganizationsDeleteRequest
  object.

  Fields:
    name: Required. The name of the ManagedOrganization to delete. Format: org
      anizations/{organization_id}/locations/*/managedOrganizations/{managed_o
      rganization_id}
  """

  name = _messages.StringField(1, required=True)


class OrglifecycleOrganizationsLocationsManagedOrganizationsGetRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsManagedOrganizationsGetRequest
  object.

  Fields:
    name: Required. The name of the ManagedOrganization to retrieve. Format: o
      rganizations/{organization_id}/locations/*/managedOrganizations/{managed
      _organization_id}
  """

  name = _messages.StringField(1, required=True)


class OrglifecycleOrganizationsLocationsManagedOrganizationsListRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsManagedOrganizationsListRequest
  object.

  Fields:
    filter: Optional. Filtering results
    orderBy: Optional. Hint for how to order the results
    pageSize: Optional. Requested page size. Server may return fewer items
      than requested. If unspecified, server will pick an appropriate default.
    pageToken: Optional. A token identifying a page of results the server
      should return.
    parent: Required. Parent value for ListManagedOrganizationsRequest
    showDeleted: Optional. Whether to return soft-deleted managed
      organizations. Default value will be false.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)
  showDeleted = _messages.BooleanField(6)


class OrglifecycleOrganizationsLocationsManagedOrganizationsPatchRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsManagedOrganizationsPatchRequest
  object.

  Fields:
    managedOrganization: A ManagedOrganization resource to be passed as the
      request body.
    name: Identifier. The resource name of the managed organization. Format: o
      rganizations/{organization_id}/locations/{location}/managedOrganizations
      /{managed_organization_id}
    updateMask: Required. Field mask is used to specify the fields to be
      overwritten in the ManagedOrganization resource by the update. The list
      of fields to update. Supported field: ManagedOrganization.admins;
      Provided admin list will replace previous list.
  """

  managedOrganization = _messages.MessageField('ManagedOrganization', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class OrglifecycleOrganizationsLocationsManagedOrganizationsUndeleteRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsManagedOrganizationsUndeleteRequest
  object.

  Fields:
    name: Required. The name of the ManagedOrganization to delete. Format: org
      anizations/{organization_id}/locations/*/managedOrganizations/{managed_o
      rganization_id}
    undeleteManagedOrganizationRequest: A UndeleteManagedOrganizationRequest
      resource to be passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  undeleteManagedOrganizationRequest = _messages.MessageField('UndeleteManagedOrganizationRequest', 2)


class OrglifecycleOrganizationsLocationsOperationsCancelRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class OrglifecycleOrganizationsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class OrglifecycleOrganizationsLocationsOperationsGetRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class OrglifecycleOrganizationsLocationsOperationsListRequest(_messages.Message):
  r"""A OrglifecycleOrganizationsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class UndeleteManagedOrganizationRequest(_messages.Message):
  r"""Message for undeleting a ManagedOrganization"""


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
