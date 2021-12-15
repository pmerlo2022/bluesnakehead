# DC1-POD2-SPINE2
# Table of Contents
<!-- toc -->

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

<!-- toc -->
# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.33.2/24 | 10.6.1.1 |

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
   ip address 10.6.33.2/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
| default | true |

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
| - | AMS DC1 DC1_POD2 DC1-POD2-SPINE2 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD2 DC1-POD2-SPINE2
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

### Global Spanning-Tree Settings


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
| Ethernet1/1 | P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet30/1 | routed | - | 172.17.2.2/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet30/1 | routed | - | 172.17.2.10/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet30/1 | routed | - | 172.17.2.18/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet30/1 | routed | - | 172.17.2.26/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet30/1 | routed | - | 172.17.2.34/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet30/1 | routed | - | 172.17.2.42/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet30/1 | routed | - | 172.17.2.50/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet30/1 | routed | - | 172.17.2.58/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet30/1 | routed | - | 172.17.2.66/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet30/1 | routed | - | 172.17.2.74/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet30/1 | routed | - | 172.17.2.82/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet30/1 | routed | - | 172.17.2.90/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet30/1 | routed | - | 172.17.2.98/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet30/1 | routed | - | 172.17.2.106/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet30/1 | routed | - | 172.17.2.114/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet30/1 | routed | - | 172.17.2.122/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet30/1 | routed | - | 172.17.2.130/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet30/1 | routed | - | 172.17.2.138/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet30/1 | routed | - | 172.17.2.146/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet30/1 | routed | - | 172.17.2.154/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet30/1 | routed | - | 172.17.2.162/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet30/1 | routed | - | 172.17.2.170/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet30/1 | routed | - | 172.17.2.178/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet30/1 | routed | - | 172.17.2.186/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet30/1 | routed | - | 172.17.2.194/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet30/1 | routed | - | 172.17.2.202/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet30/1 | routed | - | 172.17.2.210/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet30/1 | routed | - | 172.17.2.218/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet6/1 | routed | - | 172.16.2.3/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet6/1 | routed | - | 172.16.2.67/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet6/1 | routed | - | 172.16.2.131/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet6/1 | routed | - | 172.16.2.195/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.2/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.10/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.18/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.26/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.34/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.42/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.50/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.58/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.66/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.74/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.82/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.90/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.98/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.106/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.114/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.122/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.130/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.138/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.146/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.154/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.162/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.170/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.178/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.186/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.194/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.202/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.210/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.218/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.3/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.67/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.131/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.195/31
   ptp enable
   service-profile QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.29.2/32 |

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
   ip address 10.4.29.2/32
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
| default | true|| mgmt | false |

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
| default | false || mgmt | false |


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
| 65001.200|  10.4.29.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 16 ecmp 16 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Send-community | Maximum-routes |
| -------- | --------- | --- | -------------- | -------------- |
| 172.16.2.2 | 64101 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.66 | 64102 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.130 | 64103 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.194 | 64104 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.3 | 65112.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.11 | 65112.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.19 | 65112.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.27 | 65112.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.35 | 65112.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.43 | 65112.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.51 | 65112.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.59 | 65112.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.67 | 65112.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.75 | 65112.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.83 | 65112.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.91 | 65112.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.99 | 65112.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.107 | 65112.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.115 | 65112.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.123 | 65112.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.131 | 65112.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.139 | 65112.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.147 | 65112.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.155 | 65112.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.163 | 65112.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.171 | 65112.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.179 | 65112.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.187 | 65112.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.195 | 65112.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.203 | 65112.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.211 | 65112.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.219 | 65112.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

### Router BGP Device Configuration

```eos
!
router bgp 65001.200
   router-id 10.4.29.2
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 16 ecmp 16
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.2.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.2 remote-as 64101
   neighbor 172.16.2.2 description SUPER-SPINE1_Ethernet6/1
   neighbor 172.16.2.66 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.66 remote-as 64102
   neighbor 172.16.2.66 description SUPER-SPINE2_Ethernet6/1
   neighbor 172.16.2.130 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.130 remote-as 64103
   neighbor 172.16.2.130 description SUPER-SPINE3_Ethernet6/1
   neighbor 172.16.2.194 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.194 remote-as 64104
   neighbor 172.16.2.194 description SUPER-SPINE4_Ethernet6/1
   neighbor 172.17.2.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.3 remote-as 65112.100
   neighbor 172.17.2.3 description DC1-POD2-LEAF1A_Ethernet30/1
   neighbor 172.17.2.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.11 remote-as 65112.100
   neighbor 172.17.2.11 description DC1-POD2-LEAF1B_Ethernet30/1
   neighbor 172.17.2.19 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.19 remote-as 65112.200
   neighbor 172.17.2.19 description DC1-POD2-LEAF2A_Ethernet30/1
   neighbor 172.17.2.27 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.27 remote-as 65112.200
   neighbor 172.17.2.27 description DC1-POD2-LEAF2B_Ethernet30/1
   neighbor 172.17.2.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.35 remote-as 65112.300
   neighbor 172.17.2.35 description DC1-POD2-LEAF3A_Ethernet30/1
   neighbor 172.17.2.43 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.43 remote-as 65112.300
   neighbor 172.17.2.43 description DC1-POD2-LEAF3B_Ethernet30/1
   neighbor 172.17.2.51 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.51 remote-as 65112.400
   neighbor 172.17.2.51 description DC1-POD2-LEAF4A_Ethernet30/1
   neighbor 172.17.2.59 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.59 remote-as 65112.400
   neighbor 172.17.2.59 description DC1-POD2-LEAF4B_Ethernet30/1
   neighbor 172.17.2.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.67 remote-as 65112.500
   neighbor 172.17.2.67 description DC1-POD2-LEAF5A_Ethernet30/1
   neighbor 172.17.2.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.75 remote-as 65112.500
   neighbor 172.17.2.75 description DC1-POD2-LEAF5B_Ethernet30/1
   neighbor 172.17.2.83 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.83 remote-as 65112.600
   neighbor 172.17.2.83 description DC1-POD2-LEAF6A_Ethernet30/1
   neighbor 172.17.2.91 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.91 remote-as 65112.600
   neighbor 172.17.2.91 description DC1-POD2-LEAF6B_Ethernet30/1
   neighbor 172.17.2.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.99 remote-as 65112.700
   neighbor 172.17.2.99 description DC1-POD2-LEAF7A_Ethernet30/1
   neighbor 172.17.2.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.107 remote-as 65112.700
   neighbor 172.17.2.107 description DC1-POD2-LEAF7B_Ethernet30/1
   neighbor 172.17.2.115 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.115 remote-as 65112.800
   neighbor 172.17.2.115 description DC1-POD2-LEAF8A_Ethernet30/1
   neighbor 172.17.2.123 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.123 remote-as 65112.800
   neighbor 172.17.2.123 description DC1-POD2-LEAF8B_Ethernet30/1
   neighbor 172.17.2.131 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.131 remote-as 65112.900
   neighbor 172.17.2.131 description DC1-POD2-LEAF9A_Ethernet30/1
   neighbor 172.17.2.139 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.139 remote-as 65112.900
   neighbor 172.17.2.139 description DC1-POD2-LEAF9B_Ethernet30/1
   neighbor 172.17.2.147 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.147 remote-as 65112.1000
   neighbor 172.17.2.147 description DC1-POD2-LEAF10A_Ethernet30/1
   neighbor 172.17.2.155 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.155 remote-as 65112.1000
   neighbor 172.17.2.155 description DC1-POD2-LEAF10B_Ethernet30/1
   neighbor 172.17.2.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.163 remote-as 65112.1100
   neighbor 172.17.2.163 description DC1-POD2-LEAF11A_Ethernet30/1
   neighbor 172.17.2.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.171 remote-as 65112.1100
   neighbor 172.17.2.171 description DC1-POD2-LEAF11B_Ethernet30/1
   neighbor 172.17.2.179 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.179 remote-as 65112.1200
   neighbor 172.17.2.179 description DC1-POD2-LEAF12A_Ethernet30/1
   neighbor 172.17.2.187 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.187 remote-as 65112.1200
   neighbor 172.17.2.187 description DC1-POD2-LEAF12B_Ethernet30/1
   neighbor 172.17.2.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.195 remote-as 65112.1300
   neighbor 172.17.2.195 description DC1-POD2-LEAF13A_Ethernet30/1
   neighbor 172.17.2.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.203 remote-as 65112.1300
   neighbor 172.17.2.203 description DC1-POD2-LEAF13B_Ethernet30/1
   neighbor 172.17.2.211 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.211 remote-as 65112.1400
   neighbor 172.17.2.211 description DC1-POD2-LEAF14A_Ethernet30/1
   neighbor 172.17.2.219 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.219 remote-as 65112.1400
   neighbor 172.17.2.219 description DC1-POD2-LEAF14B_Ethernet30/1
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
| 10 | permit 10.4.29.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.29.0/24 eq 32
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
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

```
