# DC1-POD1-SPINE4
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
| Management0 | oob_management | oob | mgmt | 10.6.1.4/24 | 10.64.1.1 |

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
   ip address 10.6.1.4/24
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
| - | AMS DC1 DC1_POD1 DC1-POD1-SPINE4 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-SPINE4
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
| Ethernet1/1 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet32/1 | routed | - | 172.17.1.38/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet32/1 | routed | - | 172.17.1.46/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet32/1 | routed | - | 172.17.1.54/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet32/1 | routed | - | 172.17.1.62/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet32/1 | routed | - | 172.17.1.70/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet32/1 | routed | - | 172.17.1.78/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet32/1 | routed | - | 172.17.1.86/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet32/1 | routed | - | 172.17.1.94/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet32/1 | routed | - | 172.17.1.102/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet32/1 | routed | - | 172.17.1.110/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet32/1 | routed | - | 172.17.1.118/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet32/1 | routed | - | 172.17.1.126/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet32/1 | routed | - | 172.17.1.134/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet32/1 | routed | - | 172.17.1.142/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet32/1 | routed | - | 172.17.1.150/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet32/1 | routed | - | 172.17.1.158/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet32/1 | routed | - | 172.17.1.166/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet32/1 | routed | - | 172.17.1.174/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet32/1 | routed | - | 172.17.1.182/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet32/1 | routed | - | 172.17.1.190/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet32/1 | routed | - | 172.17.1.198/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet32/1 | routed | - | 172.17.1.206/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet32/1 | routed | - | 172.17.1.214/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet32/1 | routed | - | 172.17.1.222/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet32/1 | routed | - | 172.17.1.230/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet32/1 | routed | - | 172.17.1.238/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet32/1 | routed | - | 172.17.1.246/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet32/1 | routed | - | 172.17.1.254/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet4/1 | routed | - | 172.16.1.7/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet4/1 | routed | - | 172.16.1.15/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet4/1 | routed | - | 172.16.1.23/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet4/1 | routed | - | 172.16.1.31/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.38/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.46/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.54/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.62/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.70/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.78/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.86/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.94/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.102/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.110/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.118/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.126/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.134/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.142/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.150/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.158/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.166/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.174/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.182/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.190/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.198/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.206/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.214/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.222/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.230/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.238/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.246/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet32/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.254/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.7/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.15/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.23/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.31/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.28.4/32 |

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
   ip address 10.4.28.4/32
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
| mgmt  | 0.0.0.0/0 |  10.64.1.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.64.1.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001.100|  10.4.28.4 |

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
| 172.16.1.6 | 64101 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.14 | 64102 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.22 | 64103 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.30 | 64104 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.39 | 65111.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.47 | 65111.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.55 | 65111.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.63 | 65111.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.71 | 65111.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.79 | 65111.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.87 | 65111.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.95 | 65111.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.103 | 65111.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.111 | 65111.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.119 | 65111.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.127 | 65111.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.135 | 65111.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.143 | 65111.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.151 | 65111.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.159 | 65111.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.167 | 65111.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.175 | 65111.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.183 | 65111.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.191 | 65111.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.199 | 65111.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.207 | 65111.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.215 | 65111.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.223 | 65111.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.231 | 65111.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.239 | 65111.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.247 | 65111.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.255 | 65111.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

### Router BGP Device Configuration

```eos
!
router bgp 65001.100
   router-id 10.4.28.4
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 16 ecmp 16
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.1.6 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.6 remote-as 64101
   neighbor 172.16.1.6 description SUPER-SPINE1_Ethernet4/1
   neighbor 172.16.1.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.14 remote-as 64102
   neighbor 172.16.1.14 description SUPER-SPINE2_Ethernet4/1
   neighbor 172.16.1.22 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.22 remote-as 64103
   neighbor 172.16.1.22 description SUPER-SPINE3_Ethernet4/1
   neighbor 172.16.1.30 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.30 remote-as 64104
   neighbor 172.16.1.30 description SUPER-SPINE4_Ethernet4/1
   neighbor 172.17.1.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.39 remote-as 65111.100
   neighbor 172.17.1.39 description DC1-POD1-LEAF1A_Ethernet32/1
   neighbor 172.17.1.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.47 remote-as 65111.100
   neighbor 172.17.1.47 description DC1-POD1-LEAF1B_Ethernet32/1
   neighbor 172.17.1.55 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.55 remote-as 65111.200
   neighbor 172.17.1.55 description DC1-POD1-LEAF2A_Ethernet32/1
   neighbor 172.17.1.63 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.63 remote-as 65111.200
   neighbor 172.17.1.63 description DC1-POD1-LEAF2B_Ethernet32/1
   neighbor 172.17.1.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.71 remote-as 65111.300
   neighbor 172.17.1.71 description DC1-POD1-LEAF3A_Ethernet32/1
   neighbor 172.17.1.79 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.79 remote-as 65111.300
   neighbor 172.17.1.79 description DC1-POD1-LEAF3B_Ethernet32/1
   neighbor 172.17.1.87 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.87 remote-as 65111.400
   neighbor 172.17.1.87 description DC1-POD1-LEAF4A_Ethernet32/1
   neighbor 172.17.1.95 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.95 remote-as 65111.400
   neighbor 172.17.1.95 description DC1-POD1-LEAF4B_Ethernet32/1
   neighbor 172.17.1.103 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.103 remote-as 65111.500
   neighbor 172.17.1.103 description DC1-POD1-LEAF5A_Ethernet32/1
   neighbor 172.17.1.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.111 remote-as 65111.500
   neighbor 172.17.1.111 description DC1-POD1-LEAF5B_Ethernet32/1
   neighbor 172.17.1.119 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.119 remote-as 65111.600
   neighbor 172.17.1.119 description DC1-POD1-LEAF6A_Ethernet32/1
   neighbor 172.17.1.127 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.127 remote-as 65111.600
   neighbor 172.17.1.127 description DC1-POD1-LEAF6B_Ethernet32/1
   neighbor 172.17.1.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.135 remote-as 65111.700
   neighbor 172.17.1.135 description DC1-POD1-LEAF7A_Ethernet32/1
   neighbor 172.17.1.143 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.143 remote-as 65111.700
   neighbor 172.17.1.143 description DC1-POD1-LEAF7B_Ethernet32/1
   neighbor 172.17.1.151 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.151 remote-as 65111.800
   neighbor 172.17.1.151 description DC1-POD1-LEAF8A_Ethernet32/1
   neighbor 172.17.1.159 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.159 remote-as 65111.800
   neighbor 172.17.1.159 description DC1-POD1-LEAF8B_Ethernet32/1
   neighbor 172.17.1.167 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.167 remote-as 65111.900
   neighbor 172.17.1.167 description DC1-POD1-LEAF9A_Ethernet32/1
   neighbor 172.17.1.175 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.175 remote-as 65111.900
   neighbor 172.17.1.175 description DC1-POD1-LEAF9B_Ethernet32/1
   neighbor 172.17.1.183 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.183 remote-as 65111.1000
   neighbor 172.17.1.183 description DC1-POD1-LEAF10A_Ethernet32/1
   neighbor 172.17.1.191 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.191 remote-as 65111.1000
   neighbor 172.17.1.191 description DC1-POD1-LEAF10B_Ethernet32/1
   neighbor 172.17.1.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.199 remote-as 65111.1100
   neighbor 172.17.1.199 description DC1-POD1-LEAF11A_Ethernet32/1
   neighbor 172.17.1.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.207 remote-as 65111.1100
   neighbor 172.17.1.207 description DC1-POD1-LEAF11B_Ethernet32/1
   neighbor 172.17.1.215 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.215 remote-as 65111.1200
   neighbor 172.17.1.215 description DC1-POD1-LEAF12A_Ethernet32/1
   neighbor 172.17.1.223 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.223 remote-as 65111.1200
   neighbor 172.17.1.223 description DC1-POD1-LEAF12B_Ethernet32/1
   neighbor 172.17.1.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.231 remote-as 65111.1300
   neighbor 172.17.1.231 description DC1-POD1-LEAF13A_Ethernet32/1
   neighbor 172.17.1.239 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.239 remote-as 65111.1300
   neighbor 172.17.1.239 description DC1-POD1-LEAF13B_Ethernet32/1
   neighbor 172.17.1.247 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.247 remote-as 65111.1400
   neighbor 172.17.1.247 description DC1-POD1-LEAF14A_Ethernet32/1
   neighbor 172.17.1.255 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.255 remote-as 65111.1400
   neighbor 172.17.1.255 description DC1-POD1-LEAF14B_Ethernet32/1
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
| 10 | permit 10.4.28.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.28.0/24 eq 32
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
