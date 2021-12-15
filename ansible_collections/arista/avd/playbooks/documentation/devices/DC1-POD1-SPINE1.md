# DC1-POD1-SPINE1
# Table of Contents
<!-- toc -->

- [Management](#management)
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
| - | AMS DC1 DC1_POD1 DC1-POD1-SPINE1 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-SPINE1
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
| Ethernet1/1 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet29/1 | routed | - | 172.17.1.0/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet29/1 | routed | - | 172.17.1.8/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet4 | P2P_LINK_TO_DC2-POD1-LEAF14A_Ethernet29/1 | routed | - | 172.17.32.16/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet5 | P2P_LINK_TO_DC2-POD1-LEAF14B_Ethernet29/1 | routed | - | 172.17.32.24/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet29/1 | routed | - | 172.17.1.16/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet29/1 | routed | - | 172.17.1.24/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet1/1 | routed | - | 172.16.1.1/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet1/1 | routed | - | 172.16.1.9/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet1/1 | routed | - | 172.16.1.17/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet1/1 | routed | - | 172.16.1.25/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.0/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.8/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet4
   description P2P_LINK_TO_DC2-POD1-LEAF14A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet5
   description P2P_LINK_TO_DC2-POD1-LEAF14B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.16/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.1.24/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.1/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.9/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.17/31
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet1/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.25/31
   ptp enable
   service-profile QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.28.1/32 |

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
   ip address 10.4.28.1/32
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
| 65001.100|  10.4.28.1 |

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

| Neighbor | Remote AS | VRF | Send-community | Maximum-routes |
| -------- | --------- | --- | -------------- | -------------- |
| 172.16.1.0 | 65100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.8 | 65100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.16 | 65100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.24 | 65100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.1 | 65111.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.9 | 65111.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.17 | 65111.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.1.25 | 65111.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.32.17 | 65211.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.32.25 | 65211.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

### Router BGP Device Configuration

```eos
!
router bgp 65001.100
   router-id 10.4.28.1
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.1.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.0 remote-as 65100
   neighbor 172.16.1.0 description SUPER-SPINE1_Ethernet1/1
   neighbor 172.16.1.8 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.8 remote-as 65100
   neighbor 172.16.1.8 description SUPER-SPINE2_Ethernet1/1
   neighbor 172.16.1.16 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.16 remote-as 65100
   neighbor 172.16.1.16 description SUPER-SPINE3_Ethernet1/1
   neighbor 172.16.1.24 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.24 remote-as 65100
   neighbor 172.16.1.24 description SUPER-SPINE4_Ethernet1/1
   neighbor 172.17.1.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.1 remote-as 65111.100
   neighbor 172.17.1.1 description DC1-POD1-LEAF1A_Ethernet29/1
   neighbor 172.17.1.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.9 remote-as 65111.100
   neighbor 172.17.1.9 description DC1-POD1-LEAF1B_Ethernet29/1
   neighbor 172.17.1.17 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.17 remote-as 65111.1400
   neighbor 172.17.1.17 description DC1-POD1-LEAF14A_Ethernet29/1
   neighbor 172.17.1.25 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.1.25 remote-as 65111.1400
   neighbor 172.17.1.25 description DC1-POD1-LEAF14B_Ethernet29/1
   neighbor 172.17.32.17 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.17 remote-as 65211.1400
   neighbor 172.17.32.17 description DC2-POD1-LEAF14A_Ethernet29/1
   neighbor 172.17.32.25 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.25 remote-as 65211.1400
   neighbor 172.17.32.25 description DC2-POD1-LEAF14B_Ethernet29/1
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
