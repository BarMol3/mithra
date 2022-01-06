const accessTokenKey = 'access-token'
const refreshTokenKey = 'refresh-token'

// Tools
const stages = [
  { id: 1, value: 'OSINT' },
  { id: 2, value: 'Enumeration' },
  { id: 3, value: 'Vulnerabilities' },
  { id: 4, value: 'Services' },
  { id: 5, value: 'Exploitation' }
]

// Findings
const findingTypes = ['OSINT', 'Host', 'Enumeration', 'Endpoint', 'Technology', 'Vulnerability', 'Exploit', 'Credential', 'Wordlist']
const osTypesWithIcons = [
  { value: 'Linux', icon: 'brands/linux', color: 'black', variant: 'warning' },
  { value: 'Windows', icon: 'brands/windows', color: 'darkblue', variant: 'primary' },
  { value: 'MacOS', icon: 'brands/apple', color: 'gray', variant: 'secondary' },
  { value: 'iOS', icon: 'brands/apple', color: 'gray', variant: 'secondary' },
  { value: 'Android', icon: 'brands/android', color: 'forestgreen', variant: 'success' },
  { value: 'Solaris', icon: 'sun', color: 'orange', variant: 'warning' },
  { value: 'FreeBSD', icon: 'brands/freebsd', color: 'red', variant: 'danger' },
  { value: 'Other', icon: 'desktop', color: 'black', variant: 'dark' },
]
const portStatusByVariant = [
  { value: 'Open', variant: 'success' },
  { value: 'Open -Filtered', variant: 'primary' },
  { value: 'Filtered', variant: 'warning' },
  { value: 'Closed', variant: 'danger' }
]
const severities = ['Critical', 'High', 'Medium', 'Low', 'Info']
const severityByVariant = [
  { value: 'Critical', variant: 'danger' },
  { value: 'High', variant: 'warning' },
  { value: 'Medium', variant: 'primary' },
  { value: 'Low', variant: 'success' },
  { value: 'Info', variant: 'info' }
]

// Users
const roles = ['Admin', 'Auditor', 'Reader']
const auditor = ['Admin', 'Auditor']
const rolesByVariant = {
  admin: 'success',
  auditor: 'danger',
  reader: 'primary'
}
const notificationScopes = ['Disabled', 'Only my executions', 'All executions']

// Targets
const targetTypes = ['Domain', 'IP range', 'Network', 'Private IP', 'Public IP']

// Tasks
const intensitiesByVariant = [
  { intensity_rank: 'Insane', variant: 'danger' },
  { intensity_rank: 'Hard', variant: 'warning' },
  { intensity_rank: 'Normal', variant: 'secondary' },
  { intensity_rank: 'Low', variant: 'success' },
  { intensity_rank: 'Sneaky', variant: 'info' }
]
const intensitiesByValue = [
  { value: 1, text: 'Sneaky' },
  { value: 2, text: 'Low' },
  { value: 3, text: 'Normal' },
  { value: 4, text: 'Hard' },
  { value: 5, text: 'Insane' }
]
const statuses = ['Requested', 'Skipped', 'Running', 'Cancelled', 'Error', 'Completed']
const statusesByVariant = [
  { value: 'Requested', variant: 'primary' },
  { value: 'Skipped', variant: 'secondary' },
  { value: 'Running', variant: 'warning' },
  { value: 'Cancelled', variant: 'danger' },
  { value: 'Error', variant: 'danger' },
  { value: 'Completed', variant: 'success' }
]
const cancellableStatuses = ['Requested', 'Running']

export {
  accessTokenKey,
  refreshTokenKey,
  stages,
  findingTypes,
  osTypesWithIcons,
  portStatusByVariant,
  severities,
  severityByVariant,
  roles,
  rolesByVariant,
  auditor,
  notificationScopes,
  targetTypes,
  intensitiesByVariant,
  intensitiesByValue,
  statuses,
  statusesByVariant,
  cancellableStatuses
}
