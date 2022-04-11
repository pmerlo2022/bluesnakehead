# DC1-POD1-SPINE1
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.1.10/24 | 10.6.1.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 10.6.1.10/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---- | ----- |
| False | True |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$82gqIqw8b3nibNrk$MoZO0S8QMQN8uwnR8v48dbGrL0Ec/6q36tSx8y9IsExi4L.HtmokW9rX8VehLxhg542mNTBKqxMBF.LgnCTm4.
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | AMS DC1 DC1_POD1 DC1-POD1-SPINE1 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-SPINE1
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet29/1 | routed | - | 172.17.2.96/31 | default | 9214 | false | - | - |
| Ethernet1/2 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet29/2 | routed | - | 172.17.2.98/31 | default | 9214 | false | - | - |
| Ethernet1/3 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet29/1 | routed | - | 172.17.2.128/31 | default | 9214 | false | - | - |
| Ethernet1/4 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet29/2 | routed | - | 172.17.2.130/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet29/1 | routed | - | 172.17.2.160/31 | default | 9214 | false | - | - |
| Ethernet2/2 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet29/2 | routed | - | 172.17.2.162/31 | default | 9214 | false | - | - |
| Ethernet2/3 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet29/1 | routed | - | 172.17.2.192/31 | default | 9214 | false | - | - |
| Ethernet2/4 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet29/2 | routed | - | 172.17.2.194/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet29/1 | routed | - | 172.17.2.224/31 | default | 9214 | false | - | - |
| Ethernet3/2 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet29/2 | routed | - | 172.17.2.226/31 | default | 9214 | false | - | - |
| Ethernet3/3 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet29/1 | routed | - | 172.17.3.0/31 | default | 9214 | false | - | - |
| Ethernet3/4 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet29/2 | routed | - | 172.17.3.2/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet29/1 | routed | - | 172.17.3.32/31 | default | 9214 | false | - | - |
| Ethernet4/2 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet29/2 | routed | - | 172.17.3.34/31 | default | 9214 | false | - | - |
| Ethernet4/3 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet29/1 | routed | - | 172.17.3.64/31 | default | 9214 | false | - | - |
| Ethernet4/4 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet29/2 | routed | - | 172.17.3.66/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet29/1 | routed | - | 172.17.3.96/31 | default | 9214 | false | - | - |
| Ethernet5/2 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet29/2 | routed | - | 172.17.3.98/31 | default | 9214 | false | - | - |
| Ethernet5/3 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet29/1 | routed | - | 172.17.3.128/31 | default | 9214 | false | - | - |
| Ethernet5/4 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet29/2 | routed | - | 172.17.3.130/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet29/1 | routed | - | 172.17.3.160/31 | default | 9214 | false | - | - |
| Ethernet6/2 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet29/2 | routed | - | 172.17.3.162/31 | default | 9214 | false | - | - |
| Ethernet6/3 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet29/1 | routed | - | 172.17.3.192/31 | default | 9214 | false | - | - |
| Ethernet6/4 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet29/2 | routed | - | 172.17.3.194/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet29/1 | routed | - | 172.17.3.224/31 | default | 9214 | false | - | - |
| Ethernet7/2 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet29/2 | routed | - | 172.17.3.226/31 | default | 9214 | false | - | - |
| Ethernet7/3 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet29/1 | routed | - | 172.17.4.0/31 | default | 9214 | false | - | - |
| Ethernet7/4 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet29/2 | routed | - | 172.17.4.2/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet29/1 | routed | - | 172.17.4.32/31 | default | 9214 | false | - | - |
| Ethernet8/2 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet29/2 | routed | - | 172.17.4.34/31 | default | 9214 | false | - | - |
| Ethernet8/3 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet29/1 | routed | - | 172.17.4.64/31 | default | 9214 | false | - | - |
| Ethernet8/4 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet29/2 | routed | - | 172.17.4.66/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet29/1 | routed | - | 172.17.4.96/31 | default | 9214 | false | - | - |
| Ethernet9/2 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet29/2 | routed | - | 172.17.4.98/31 | default | 9214 | false | - | - |
| Ethernet9/3 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet29/1 | routed | - | 172.17.4.128/31 | default | 9214 | false | - | - |
| Ethernet9/4 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet29/2 | routed | - | 172.17.4.130/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet29/1 | routed | - | 172.17.4.160/31 | default | 9214 | false | - | - |
| Ethernet10/2 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet29/2 | routed | - | 172.17.4.162/31 | default | 9214 | false | - | - |
| Ethernet10/3 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet29/1 | routed | - | 172.17.4.192/31 | default | 9214 | false | - | - |
| Ethernet10/4 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet29/2 | routed | - | 172.17.4.194/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet29/1 | routed | - | 172.17.4.224/31 | default | 9214 | false | - | - |
| Ethernet11/2 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet29/2 | routed | - | 172.17.4.226/31 | default | 9214 | false | - | - |
| Ethernet11/3 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet29/1 | routed | - | 172.17.5.0/31 | default | 9214 | false | - | - |
| Ethernet11/4 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet29/2 | routed | - | 172.17.5.2/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet29/1 | routed | - | 172.17.5.32/31 | default | 9214 | false | - | - |
| Ethernet12/2 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet29/2 | routed | - | 172.17.5.34/31 | default | 9214 | false | - | - |
| Ethernet12/3 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet29/1 | routed | - | 172.17.5.64/31 | default | 9214 | false | - | - |
| Ethernet12/4 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet29/2 | routed | - | 172.17.5.66/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet29/1 | routed | - | 172.17.5.96/31 | default | 9214 | false | - | - |
| Ethernet13/2 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet29/2 | routed | - | 172.17.5.98/31 | default | 9214 | false | - | - |
| Ethernet13/3 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet29/1 | routed | - | 172.17.5.128/31 | default | 9214 | false | - | - |
| Ethernet13/4 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet29/2 | routed | - | 172.17.5.130/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet29/1 | routed | - | 172.17.5.160/31 | default | 9214 | false | - | - |
| Ethernet14/2 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet29/2 | routed | - | 172.17.5.162/31 | default | 9214 | false | - | - |
| Ethernet14/3 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet29/1 | routed | - | 172.17.5.192/31 | default | 9214 | false | - | - |
| Ethernet14/4 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet29/2 | routed | - | 172.17.5.194/31 | default | 9214 | false | - | - |
| Ethernet29/2 | P2P_LINK_TO_SUPER-SPINE1_Ethernet1/1 | routed | - | 172.16.0.19/31 | default | 9214 | false | - | - |
| Ethernet30/2 | P2P_LINK_TO_SUPER-SPINE2_Ethernet1/1 | routed | - | 172.16.0.27/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet1/1 | routed | - | 172.16.0.35/31 | default | 9214 | false | - | - |
| Ethernet32/2 | P2P_LINK_TO_SUPER-SPINE4_Ethernet1/1 | routed | - | 172.16.0.43/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.96/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/2
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.98/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/3
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.128/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/4
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.130/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.160/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/2
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.162/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/3
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.192/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/4
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.194/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.224/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/2
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.226/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/3
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.0/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/4
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.2/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.32/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/2
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.34/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/3
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.64/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/4
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.66/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.96/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/2
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.98/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/3
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.128/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/4
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.130/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.160/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/2
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.162/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/3
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.192/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/4
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.194/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.224/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/2
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.226/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/3
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.0/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/4
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.2/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.32/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/2
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.34/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/3
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.64/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/4
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.66/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.96/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/2
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.98/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/3
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.128/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/4
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.130/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.160/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/2
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.162/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/3
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.192/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/4
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.194/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.224/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/2
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.226/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/3
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.0/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/4
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.2/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.32/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/2
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.34/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/3
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.64/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/4
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.66/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.96/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/2
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.98/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/3
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.128/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/4
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.130/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.160/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/2
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.162/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/3
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet29/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.192/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/4
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet29/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.194/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/2
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.19/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/2
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.27/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.35/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/2
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.43/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.0.10/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.0.10/32
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| mgmt | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.1.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.1.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 64601|  10.4.0.10 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- |
| 172.16.0.18 | 64501 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.26 | 64502 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.34 | 64503 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.42 | 64504 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.97 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.99 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.129 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.131 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.161 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.163 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.193 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.195 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.225 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.227 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.1 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.3 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.33 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.35 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.65 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.67 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.97 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.99 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.129 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.131 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.161 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.163 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.193 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.195 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.225 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.227 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.1 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.3 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.33 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.35 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.65 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.67 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.97 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.99 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.129 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.131 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.161 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.163 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.193 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.195 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.225 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.227 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.1 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.3 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.33 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.35 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.65 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.67 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.97 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.99 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.129 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.131 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.161 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.163 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.193 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.195 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 64601
   router-id 10.4.0.10
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.0.18 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.18 remote-as 64501
   neighbor 172.16.0.18 description SUPER-SPINE1_Ethernet1/1
   neighbor 172.16.0.26 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.26 remote-as 64502
   neighbor 172.16.0.26 description SUPER-SPINE2_Ethernet1/1
   neighbor 172.16.0.34 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.34 remote-as 64503
   neighbor 172.16.0.34 description SUPER-SPINE3_Ethernet1/1
   neighbor 172.16.0.42 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.42 remote-as 64504
   neighbor 172.16.0.42 description SUPER-SPINE4_Ethernet1/1
   neighbor 172.17.2.97 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.97 remote-as 64901
   neighbor 172.17.2.97 description DC1-POD1-LEAF1A_Ethernet29/1
   neighbor 172.17.2.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.99 remote-as 64901
   neighbor 172.17.2.99 description DC1-POD1-LEAF1A_Ethernet29/2
   neighbor 172.17.2.129 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.129 remote-as 64901
   neighbor 172.17.2.129 description DC1-POD1-LEAF1B_Ethernet29/1
   neighbor 172.17.2.131 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.131 remote-as 64901
   neighbor 172.17.2.131 description DC1-POD1-LEAF1B_Ethernet29/2
   neighbor 172.17.2.161 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.161 remote-as 64902
   neighbor 172.17.2.161 description DC1-POD1-LEAF2A_Ethernet29/1
   neighbor 172.17.2.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.163 remote-as 64902
   neighbor 172.17.2.163 description DC1-POD1-LEAF2A_Ethernet29/2
   neighbor 172.17.2.193 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.193 remote-as 64902
   neighbor 172.17.2.193 description DC1-POD1-LEAF2B_Ethernet29/1
   neighbor 172.17.2.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.195 remote-as 64902
   neighbor 172.17.2.195 description DC1-POD1-LEAF2B_Ethernet29/2
   neighbor 172.17.2.225 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.225 remote-as 64903
   neighbor 172.17.2.225 description DC1-POD1-LEAF3A_Ethernet29/1
   neighbor 172.17.2.227 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.227 remote-as 64903
   neighbor 172.17.2.227 description DC1-POD1-LEAF3A_Ethernet29/2
   neighbor 172.17.3.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.1 remote-as 64903
   neighbor 172.17.3.1 description DC1-POD1-LEAF3B_Ethernet29/1
   neighbor 172.17.3.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.3 remote-as 64903
   neighbor 172.17.3.3 description DC1-POD1-LEAF3B_Ethernet29/2
   neighbor 172.17.3.33 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.33 remote-as 64904
   neighbor 172.17.3.33 description DC1-POD1-LEAF4A_Ethernet29/1
   neighbor 172.17.3.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.35 remote-as 64904
   neighbor 172.17.3.35 description DC1-POD1-LEAF4A_Ethernet29/2
   neighbor 172.17.3.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.65 remote-as 64904
   neighbor 172.17.3.65 description DC1-POD1-LEAF4B_Ethernet29/1
   neighbor 172.17.3.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.67 remote-as 64904
   neighbor 172.17.3.67 description DC1-POD1-LEAF4B_Ethernet29/2
   neighbor 172.17.3.97 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.97 remote-as 64905
   neighbor 172.17.3.97 description DC1-POD1-LEAF5A_Ethernet29/1
   neighbor 172.17.3.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.99 remote-as 64905
   neighbor 172.17.3.99 description DC1-POD1-LEAF5A_Ethernet29/2
   neighbor 172.17.3.129 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.129 remote-as 64905
   neighbor 172.17.3.129 description DC1-POD1-LEAF5B_Ethernet29/1
   neighbor 172.17.3.131 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.131 remote-as 64905
   neighbor 172.17.3.131 description DC1-POD1-LEAF5B_Ethernet29/2
   neighbor 172.17.3.161 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.161 remote-as 64906
   neighbor 172.17.3.161 description DC1-POD1-LEAF6A_Ethernet29/1
   neighbor 172.17.3.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.163 remote-as 64906
   neighbor 172.17.3.163 description DC1-POD1-LEAF6A_Ethernet29/2
   neighbor 172.17.3.193 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.193 remote-as 64906
   neighbor 172.17.3.193 description DC1-POD1-LEAF6B_Ethernet29/1
   neighbor 172.17.3.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.195 remote-as 64906
   neighbor 172.17.3.195 description DC1-POD1-LEAF6B_Ethernet29/2
   neighbor 172.17.3.225 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.225 remote-as 64907
   neighbor 172.17.3.225 description DC1-POD1-LEAF7A_Ethernet29/1
   neighbor 172.17.3.227 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.227 remote-as 64907
   neighbor 172.17.3.227 description DC1-POD1-LEAF7A_Ethernet29/2
   neighbor 172.17.4.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.1 remote-as 64907
   neighbor 172.17.4.1 description DC1-POD1-LEAF7B_Ethernet29/1
   neighbor 172.17.4.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.3 remote-as 64907
   neighbor 172.17.4.3 description DC1-POD1-LEAF7B_Ethernet29/2
   neighbor 172.17.4.33 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.33 remote-as 64908
   neighbor 172.17.4.33 description DC1-POD1-LEAF8A_Ethernet29/1
   neighbor 172.17.4.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.35 remote-as 64908
   neighbor 172.17.4.35 description DC1-POD1-LEAF8A_Ethernet29/2
   neighbor 172.17.4.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.65 remote-as 64908
   neighbor 172.17.4.65 description DC1-POD1-LEAF8B_Ethernet29/1
   neighbor 172.17.4.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.67 remote-as 64908
   neighbor 172.17.4.67 description DC1-POD1-LEAF8B_Ethernet29/2
   neighbor 172.17.4.97 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.97 remote-as 64909
   neighbor 172.17.4.97 description DC1-POD1-LEAF9A_Ethernet29/1
   neighbor 172.17.4.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.99 remote-as 64909
   neighbor 172.17.4.99 description DC1-POD1-LEAF9A_Ethernet29/2
   neighbor 172.17.4.129 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.129 remote-as 64909
   neighbor 172.17.4.129 description DC1-POD1-LEAF9B_Ethernet29/1
   neighbor 172.17.4.131 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.131 remote-as 64909
   neighbor 172.17.4.131 description DC1-POD1-LEAF9B_Ethernet29/2
   neighbor 172.17.4.161 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.161 remote-as 64910
   neighbor 172.17.4.161 description DC1-POD1-LEAF10A_Ethernet29/1
   neighbor 172.17.4.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.163 remote-as 64910
   neighbor 172.17.4.163 description DC1-POD1-LEAF10A_Ethernet29/2
   neighbor 172.17.4.193 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.193 remote-as 64910
   neighbor 172.17.4.193 description DC1-POD1-LEAF10B_Ethernet29/1
   neighbor 172.17.4.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.195 remote-as 64910
   neighbor 172.17.4.195 description DC1-POD1-LEAF10B_Ethernet29/2
   neighbor 172.17.4.225 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.225 remote-as 64911
   neighbor 172.17.4.225 description DC1-POD1-LEAF11A_Ethernet29/1
   neighbor 172.17.4.227 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.227 remote-as 64911
   neighbor 172.17.4.227 description DC1-POD1-LEAF11A_Ethernet29/2
   neighbor 172.17.5.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.1 remote-as 64911
   neighbor 172.17.5.1 description DC1-POD1-LEAF11B_Ethernet29/1
   neighbor 172.17.5.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.3 remote-as 64911
   neighbor 172.17.5.3 description DC1-POD1-LEAF11B_Ethernet29/2
   neighbor 172.17.5.33 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.33 remote-as 64912
   neighbor 172.17.5.33 description DC1-POD1-LEAF12A_Ethernet29/1
   neighbor 172.17.5.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.35 remote-as 64912
   neighbor 172.17.5.35 description DC1-POD1-LEAF12A_Ethernet29/2
   neighbor 172.17.5.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.65 remote-as 64912
   neighbor 172.17.5.65 description DC1-POD1-LEAF12B_Ethernet29/1
   neighbor 172.17.5.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.67 remote-as 64912
   neighbor 172.17.5.67 description DC1-POD1-LEAF12B_Ethernet29/2
   neighbor 172.17.5.97 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.97 remote-as 64913
   neighbor 172.17.5.97 description DC1-POD1-LEAF13A_Ethernet29/1
   neighbor 172.17.5.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.99 remote-as 64913
   neighbor 172.17.5.99 description DC1-POD1-LEAF13A_Ethernet29/2
   neighbor 172.17.5.129 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.129 remote-as 64913
   neighbor 172.17.5.129 description DC1-POD1-LEAF13B_Ethernet29/1
   neighbor 172.17.5.131 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.131 remote-as 64913
   neighbor 172.17.5.131 description DC1-POD1-LEAF13B_Ethernet29/2
   neighbor 172.17.5.161 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.161 remote-as 64914
   neighbor 172.17.5.161 description DC1-POD1-LEAF14A_Ethernet29/1
   neighbor 172.17.5.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.163 remote-as 64914
   neighbor 172.17.5.163 description DC1-POD1-LEAF14A_Ethernet29/2
   neighbor 172.17.5.193 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.193 remote-as 64914
   neighbor 172.17.5.193 description DC1-POD1-LEAF14B_Ethernet29/1
   neighbor 172.17.5.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.195 remote-as 64914
   neighbor 172.17.5.195 description DC1-POD1-LEAF14B_Ethernet29/2
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

# Multicast

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.0.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.0.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB in AMS.yml

```
